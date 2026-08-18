"""Multiprocessing: several independent processes."""
import multiprocessing
import time


def wait_task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")


if __name__ == "__main__":
    start = time.perf_counter()
    processes = [
        multiprocessing.Process(target=wait_task, args=(f"task-{i}",))
        for i in range(1, 4)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Total time: {time.perf_counter() - start:.1f}s")
