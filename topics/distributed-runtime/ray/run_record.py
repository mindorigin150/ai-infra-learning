"""CLI and run records shared by the CPU and GPU Ray learning experiments."""

import argparse
import json
import os
import platform
import socket
import subprocess
import sys
import threading
import time
import traceback
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import ray


TIMEOUT_SECONDS = 120


def parse_args(kind, cases):
    parser = argparse.ArgumentParser(description=f"Ray {kind.upper()} learning experiments")
    parser.add_argument("--case", choices=[*cases, "all"], default="all")
    parser.add_argument("--num-cpus", type=int, default=4, help="Logical CPU admission capacity")
    parser.add_argument("--output", type=Path, help="New directory for run.json; existing directories are rejected")
    args = parser.parse_args()
    if args.num_cpus < 1:
        parser.error("--num-cpus must be at least 1")
    if args.output is None:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        args.output = Path(".runs") / f"ray-{kind}" / stamp
    return args


def event(label):
    """Capture a process/thread location and timestamp on this single-node run."""
    return {
        "label": label,
        "at_ns": time.perf_counter_ns(),
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "thread_id": threading.get_ident(),
    }


@contextmanager
def recorded_run(args, kind):
    """Own an isolated local runtime and persist success or failure before exiting."""
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    record = {
        "kind": f"Ray {kind} learning experiment",
        "status": "running",
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": [sys.executable, *sys.argv],
        "parameters": {"case": args.case, "num_cpus": args.num_cpus, "timeout_seconds": TIMEOUT_SECONDS},
        "clock": "time.perf_counter_ns; comparable across processes on this single node",
        "environment": {
            "hostname": socket.gethostname(),
            "platform": platform.platform(),
            "python": platform.python_version(),
            "ray": ray.__version__,
            "host_cpu_count": os.cpu_count(),
            "cpu_affinity_count": len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else None,
        },
        "cases": [],
    }
    try:
        repo = Path(__file__).resolve().parents[3]
        record["environment"]["git_revision"] = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"], cwd=repo, text=True, capture_output=True, check=True,
        ).stdout.strip()
        record["environment"]["git_status"] = subprocess.run(
            ["git", "status", "--porcelain"], cwd=repo, text=True, capture_output=True, check=True,
        ).stdout.splitlines()
        options = {"address": "local", "num_cpus": args.num_cpus, "include_dashboard": False,
                   "object_store_memory": 128 * 1024**2,
                   "runtime_env": {"working_dir": str(Path(__file__).resolve().parent)}}
        if kind == "cpu":
            options["num_gpus"] = 0
        ray.init(**options)
        record["environment"]["ray_resources"] = ray.cluster_resources()
        yield record
        record["status"] = "passed"
    except BaseException as exc:
        record["status"] = "failed"
        record["error"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        if record["cases"] and record["cases"][-1]["status"] == "running":
            record["cases"][-1]["status"] = "failed"
        raise
    finally:
        record["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
        (output / "run.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{record['status']}: {output / 'run.json'}", flush=True)
        ray.shutdown()
