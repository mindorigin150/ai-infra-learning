"""Measure CPU NumPy vector addition; record samples and environment for the lab."""

import argparse
import csv
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


def positive_int(value: str) -> int:
    """Validate positive integer values at the command-line boundary."""
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


def main() -> None:
    """Write raw timings, summaries, and provenance for a recorded CPU run."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", nargs="+", type=positive_int, default=[1024, 16384, 262144, 4194304])
    parser.add_argument("--repeats", type=positive_int, default=25)
    parser.add_argument("--warmups", type=positive_int, default=3)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--context", required=True, help="Describe where and why this run was performed.")
    args = parser.parse_args()
    rows = []
    for size in args.sizes:
        x = np.ones(size, dtype=np.float32)
        y = np.full(size, 2, dtype=np.float32)
        out = np.empty_like(x)
        for _ in range(args.warmups):
            np.add(x, y, out=out)
        samples = []
        for _ in range(args.repeats):
            started = time.perf_counter_ns()
            np.add(x, y, out=out)
            samples.append(time.perf_counter_ns() - started)
        if not np.all(out == 3):
            raise RuntimeError("vector addition produced an incorrect result")
        median_ns = float(np.median(samples))
        # Two reads and one write: useful byte count, not measured DRAM traffic.
        useful_bytes = 3 * size * x.itemsize
        rows.append({
            "elements": size,
            "useful_bytes": useful_bytes,
            "median_ns": median_ns,
            "p25_ns": float(np.percentile(samples, 25)),
            "p75_ns": float(np.percentile(samples, 75)),
            "effective_gb_s": useful_bytes / median_ns,
            "samples_ns": samples,
        })

    repo = Path(__file__).resolve().parents[3]
    revision = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=repo, text=True,
        capture_output=True, check=False,
    )
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=repo, text=True,
        capture_output=True, check=True,
    )
    if revision.returncode == 0:
        code_revision = revision.stdout.strip()
    elif revision.returncode == 128:
        code_revision = None  # Explicitly represents a repo with no commit yet.
    else:
        raise RuntimeError(revision.stderr)
    record = {
        "kind": "measured CPU experiment",
        "context": args.context,
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "platform": platform.platform(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "python": platform.python_version(),
            "numpy": np.__version__,
            "code_revision": code_revision,
            "worktree_dirty": bool(status.stdout.strip()),
        },
        "measurement": {
            "operation": "numpy.add(x, y, out=out)",
            "dtype": "float32",
            "sizes": args.sizes,
            "warmups": args.warmups,
            "repeats": args.repeats,
            "clock": "time.perf_counter_ns",
            "useful_bytes_model": "two input reads + one output write; 12 * elements",
            "limitations": "CPU host timing includes call overhead. Caches and write allocation affect actual DRAM traffic. This does not measure GPU or peak memory bandwidth.",
            "command": [sys.executable, *sys.argv],
        },
        "results": rows,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "run.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    columns = [key for key in rows[0] if key != "samples_ns"]
    with (args.output / "summary.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Recorded CPU run: {args.output}")
    for row in rows:
        print(f"{row['elements']:>9,} elements: {row['median_ns'] / 1e3:>10.2f} us, {row['effective_gb_s']:>8.2f} effective GB/s")


if __name__ == "__main__":
    main()
