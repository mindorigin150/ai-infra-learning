"""Observe Ray task submission, object dependencies, actor state and concurrency."""

import asyncio
import threading
import time

import ray

from run_record import TIMEOUT_SECONDS, event, parse_args, recorded_run


TASK_COUNT = 8
DELAY_SECONDS = 0.15  # Simulated waiting, not a CPU performance workload.


@ray.remote(num_cpus=1)
def square(number, delay=DELAY_SECONDS):
    started = event("task_start")
    time.sleep(delay)
    return {"input": number, "value": number * number, "events": [started, event("task_end")]}


@ray.remote(num_cpus=1)
def total(values):
    return {"value": sum(values), "events": [event("object_consumed")]}


@ray.remote(num_cpus=1)
def plus_one(task_result):
    return {"value": task_result["value"] + 1, "events": [event("dependency_consumed")]}


@ray.remote(num_cpus=1)
class Counter:
    """Keep a counter in one persistent actor process, using default serial calls."""

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return {"value": self.value, "events": [event("counter_increment")]}


@ray.remote(num_cpus=1)
class WaitingActor:
    """Simulate waiting with a counter safe for both serial and threaded execution."""

    def __init__(self):
        self.completed = 0
        self.lock = threading.Lock()

    def wait(self, number):
        started = event("actor_call_start")
        time.sleep(DELAY_SECONDS)
        with self.lock:
            self.completed += 1
            completed = self.completed
        return {"input": number, "completed": completed, "events": [started, event("actor_call_end")]}


@ray.remote(num_cpus=1)
class AsyncWaitingActor:
    """Yield simulated waiting to the event loop and protect shared actor state."""

    def __init__(self):
        self.completed = 0
        self.lock = asyncio.Lock()

    async def wait(self, number):
        started = event("async_call_start")
        await asyncio.sleep(DELAY_SECONDS)
        async with self.lock:
            self.completed += 1
            completed = self.completed
        return {"input": number, "completed": completed, "events": [started, event("async_call_end")]}


def tasks_case():
    observations = []
    for mode in ("submit_then_get_each", "submit_all_then_get"):
        started = time.perf_counter_ns()
        if mode == "submit_then_get_each":
            results = [ray.get(square.remote(i), timeout=TIMEOUT_SECONDS) for i in range(TASK_COUNT)]
        else:
            refs = [square.remote(i) for i in range(TASK_COUNT)]
            results = ray.get(refs, timeout=TIMEOUT_SECONDS)
        finished = time.perf_counter_ns()
        assert [r["value"] for r in results] == [i * i for i in range(TASK_COUNT)]
        observations.append({"mode": mode, "driver_elapsed_ns": finished - started, "results": results})
    return {"task_count": TASK_COUNT, "teaching_delay_seconds": DELAY_SECONDS, "observations": observations}


def objects_case():
    values = list(range(16))
    shared = ray.put(values)
    consumers = ray.get([total.remote(shared) for _ in range(2)], timeout=TIMEOUT_SECONDS)
    assert [r["value"] for r in consumers] == [sum(values)] * 2
    producer = square.remote(3, delay=0)
    dependent = ray.get(plus_one.remote(producer), timeout=TIMEOUT_SECONDS)
    assert dependent["value"] == 10
    producer_result = ray.get(producer, timeout=TIMEOUT_SECONDS)

    pending = []
    results = []
    pending_counts = []
    limit = 3
    for i in range(TASK_COUNT):
        if len(pending) == limit:
            ready, pending = ray.wait(pending, num_returns=1, timeout=TIMEOUT_SECONDS)
            if not ready:
                raise TimeoutError("No pending task became ready")
            results.extend(ray.get(ready, timeout=TIMEOUT_SECONDS))
        pending.append(square.remote(i))
        pending_counts.append(len(pending))
    results.extend(ray.get(pending, timeout=TIMEOUT_SECONDS))
    assert sorted(r["value"] for r in results) == [i * i for i in range(TASK_COUNT)]
    return {"put_consumers": consumers, "producer_result": producer_result, "dependency_result": dependent,
            "pending_limit": limit, "pending_counts_after_submission": pending_counts, "results": results}


def actor_case():
    actor = Counter.remote()
    try:
        results = ray.get([actor.increment.remote() for _ in range(3)], timeout=TIMEOUT_SECONDS)
        assert [r["value"] for r in results] == [1, 2, 3]
        assert len({r["events"][0]["pid"] for r in results}) == 1
        return {"results": results}
    finally:
        ray.kill(actor)


def concurrency_case():
    observations = []
    for mode in ("serial", "threaded", "async"):
        if mode == "serial":
            actor = WaitingActor.remote()
        elif mode == "threaded":
            actor = WaitingActor.options(max_concurrency=2).remote()
        else:
            actor = AsyncWaitingActor.options(max_concurrency=2).remote()
        try:
            started = time.perf_counter_ns()
            results = ray.get([actor.wait.remote(i) for i in range(4)], timeout=TIMEOUT_SECONDS)
            finished = time.perf_counter_ns()
            assert sorted(r["completed"] for r in results) == [1, 2, 3, 4]
            assert len({r["events"][0]["pid"] for r in results}) == 1
            if mode in ("serial", "async"):
                assert len({r["events"][0]["thread_id"] for r in results}) == 1
            observations.append({"mode": mode, "max_concurrency": 1 if mode == "serial" else 2,
                                 "driver_elapsed_ns": finished - started, "results": results})
        finally:
            ray.kill(actor)
    return {"teaching_delay_seconds": DELAY_SECONDS, "observations": observations}


def main():
    cases = {"tasks": tasks_case, "objects": objects_case, "actor": actor_case, "concurrency": concurrency_case}
    args = parse_args("cpu", cases)
    with recorded_run(args, "cpu") as record:
        for name, experiment in cases.items():
            if args.case in (name, "all"):
                case = {"name": name, "status": "running"}
                record["cases"].append(case)
                case["result"] = experiment()
                case["status"] = "passed"


if __name__ == "__main__":
    main()
