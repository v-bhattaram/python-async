"""asyncio.sleep() vs time.sleep() inside async code."""
import asyncio
import time


async def ticker():
    """Prints a tick every 0.2s, to show whether the loop is still alive."""
    for i in range(5):
        print(f"  tick {i}")
        await asyncio.sleep(0.2)


async def bad_sleep():
    print("bad_sleep: blocking with time.sleep(1) ...")
    time.sleep(1)  # BLOCKS the whole event loop - ticker cannot run during this
    print("bad_sleep: done")


async def good_sleep():
    print("good_sleep: pausing with asyncio.sleep(1) ...")
    await asyncio.sleep(1)  # lets ticker keep ticking during this
    print("good_sleep: done")


async def main():
    print("--- Using time.sleep() (blocks everything) ---")
    await asyncio.gather(ticker(), bad_sleep())

    print("\n--- Using asyncio.sleep() (lets other tasks run) ---")
    await asyncio.gather(ticker(), good_sleep())


if __name__ == "__main__":
    asyncio.run(main())
