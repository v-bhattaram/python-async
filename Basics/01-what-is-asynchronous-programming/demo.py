"""Synchronous (blocking) vs Asynchronous (non-blocking) waiting."""
import asyncio
import time


def make_tea_sync(name):
    print(f"[sync] start making {name}")
    time.sleep(2)  # blocks everything for 2 seconds
    print(f"[sync] {name} ready")


async def make_tea_async(name):
    print(f"[async] start making {name}")
    await asyncio.sleep(2)  # pauses THIS task, lets others run
    print(f"[async] {name} ready")


def run_sync_version():
    start = time.perf_counter()
    make_tea_sync("green tea")
    make_tea_sync("black tea")
    print(f"Synchronous total time: {time.perf_counter() - start:.1f}s\n")


async def run_async_version():
    start = time.perf_counter()
    # both start "at the same time" and wait together
    await asyncio.gather(
        make_tea_async("green tea"),
        make_tea_async("black tea"),
    )
    print(f"Asynchronous total time: {time.perf_counter() - start:.1f}s")


if __name__ == "__main__":
    run_sync_version()
    asyncio.run(run_async_version())
