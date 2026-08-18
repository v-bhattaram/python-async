"""asyncio.create_task() schedules a coroutine to start running now."""
import asyncio
import time


async def work(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} finished")


async def sequential():
    start = time.perf_counter()
    await work("A")   # A fully finishes before B even starts
    await work("B")
    print(f"Sequential total: {time.perf_counter() - start:.1f}s\n")


async def concurrent_with_tasks():
    start = time.perf_counter()
    task_a = asyncio.create_task(work("A"))  # starts immediately
    task_b = asyncio.create_task(work("B"))  # starts immediately too
    await task_a
    await task_b
    print(f"Concurrent total: {time.perf_counter() - start:.1f}s")


async def main():
    await sequential()
    await concurrent_with_tasks()


if __name__ == "__main__":
    asyncio.run(main())
