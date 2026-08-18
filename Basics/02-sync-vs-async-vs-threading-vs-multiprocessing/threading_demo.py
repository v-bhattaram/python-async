"""Multithreading: several threads, all in the same process."""
import threading
import time


def wait_task(name):
    print(f"{name} started")
    time.sleep(1)
    print(f"{name} finished")


start = time.perf_counter()
threads = [threading.Thread(target=wait_task, args=(f"task-{i}",)) for i in range(1, 4)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Total time: {time.perf_counter() - start:.1f}s")
