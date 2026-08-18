"""Asynchronous: one thread, tasks take turns waiting together."""
import asyncio
import time


async def wait_task(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} finished")


async def main():
    start = time.perf_counter()
    await asyncio.gather(
        wait_task("task-1"),
        wait_task("task-2"),
        wait_task("task-3"),
    )
    print(f"Total time: {time.perf_counter() - start:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())
