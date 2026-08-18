"""Watching the event loop switch between tasks."""
import asyncio


async def order(name, cook_time):
    print(f"{name} started")
    await asyncio.sleep(cook_time)  # pauses here, event loop runs other tasks
    print(f"{name} finished")


async def main():
    # asyncio.run() creates the event loop, runs main(), then closes the loop.
    await asyncio.gather(
        order("order-1", 2),
        order("order-2", 1),
        order("order-3", 3),
    )


if __name__ == "__main__":
    asyncio.run(main())  # Event Loop
