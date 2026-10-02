"""Observe one-GPU tasks and persistent actors assigned to two different GPUs."""

import os
import subprocess

import ray
import torch

from run_record import TIMEOUT_SECONDS, event, parse_args, recorded_run


ELEMENTS = 4096


def device_info():
    assigned = ray.get_runtime_context().get_accelerator_ids()["GPU"]
    assert len(assigned) == 1, assigned
    assert torch.cuda.is_available(), "PyTorch cannot use the GPU assigned by Ray"
    assert torch.cuda.device_count() == 1, "Expected one CUDA-visible GPU per worker"
    properties = torch.cuda.get_device_properties(0)
    return {"ray_gpu_ids": assigned, "cuda_visible_devices": os.environ["CUDA_VISIBLE_DEVICES"],
            "local_device": "cuda:0", "name": properties.name,
            "total_memory_bytes": properties.total_memory,
            "compute_capability": list(torch.cuda.get_device_capability(0))}


def checked_add(x, y):
    started = event("gpu_add_start")
    result = x + y
    torch.cuda.synchronize()
    finished = event("gpu_add_synchronized")
    expected = torch.arange(ELEMENTS, dtype=torch.float32) + 1
    torch.testing.assert_close(result.cpu(), expected, rtol=0, atol=0)
    return {"elements": ELEMENTS, "dtype": "float32", "correct": True,
            "events": [started, finished, event("cpu_validation_end")]}


@ray.remote(num_cpus=1, num_gpus=1)
def vector_add():
    device = device_info()
    x = torch.arange(ELEMENTS, dtype=torch.float32, device="cuda:0")
    y = torch.ones_like(x)
    return {"device": device, "computation": checked_add(x, y)}


@ray.remote(num_cpus=1, num_gpus=1)
class VectorActor:
    """Retain CUDA buffers and a call counter on one assigned GPU for its lifetime."""

    def __init__(self):
        self.device = device_info()
        self.x = torch.arange(ELEMENTS, dtype=torch.float32, device="cuda:0")
        self.y = torch.ones_like(self.x)
        self.calls = 0

    def step(self):
        computation = checked_add(self.x, self.y)
        self.calls += 1
        return {"device": self.device, "calls": self.calls, "computation": computation}


def actors_case():
    actors = []
    try:
        for _ in range(2):
            actors.append(VectorActor.remote())
        rounds = [ray.get([actor.step.remote() for actor in actors], timeout=TIMEOUT_SECONDS) for _ in range(2)]
        first, second = rounds
        assigned = [set(result["device"]["ray_gpu_ids"]) for result in first]
        assert assigned[0].isdisjoint(assigned[1]), "The two actors must hold different Ray GPU assignments"
        assert len({r["computation"]["events"][0]["pid"] for r in first}) == 2
        for i in range(2):
            assert first[i]["calls"] == 1 and second[i]["calls"] == 2
            assert first[i]["device"] == second[i]["device"]
            assert first[i]["computation"]["events"][0]["pid"] == second[i]["computation"]["events"][0]["pid"]
        return {"rounds": rounds}
    finally:
        for actor in actors:
            ray.kill(actor)


def main():
    cases = ("task", "actors")
    args = parse_args("gpu", cases)
    with recorded_run(args, "gpu") as record:
        record["parameters"].update({"elements": ELEMENTS, "dtype": "float32"})
        record["environment"].update({"torch": torch.__version__, "torch_cuda_build": torch.version.cuda,
                                      "driver_cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES")})
        record["environment"]["nvidia_smi"] = subprocess.run(
            ["nvidia-smi", "--query-gpu=index,name,uuid,memory.total,driver_version", "--format=csv"],
            text=True, capture_output=True, check=True,
        ).stdout.splitlines()
        resources = record["environment"]["ray_resources"]
        required = 2 if args.case in ("actors", "all") else 1
        if "GPU" not in resources or resources["GPU"] < required:
            raise RuntimeError(f"This case requires {required} Ray-visible GPU(s); detected resources: {resources}")
        if args.num_cpus < required:
            raise RuntimeError(f"This case needs at least {required} logical CPUs for its GPU workers")
        for name in cases:
            if args.case in (name, "all"):
                case = {"name": name, "status": "running"}
                record["cases"].append(case)
                case["result"] = ray.get(vector_add.remote(), timeout=TIMEOUT_SECONDS) if name == "task" else actors_case()
                case["status"] = "passed"


if __name__ == "__main__":
    main()
