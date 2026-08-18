"""Synchronous: each wait happens one after another."""
import time


def wait_task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")


start = time.perf_counter()
wait_task("task-1")
wait_task("task-2")
wait_task("task-3")
print(f"Total time: {time.perf_counter() - start:.1f}s")
