"""A coroutine function, and the coroutine object it creates."""
import asyncio
import inspect


async def add(a, b):
    return a + b


async def main():
    print("Is add a coroutine function?", inspect.iscoroutinefunction(add))

    coro = add(1, 2)  # calling it just builds a coroutine object
    print("Calling add(1, 2) gives:", coro)
    print("Is that a coroutine object?", inspect.iscoroutine(coro))

    result = await coro  # NOW it actually runs and gives us 3
    print("Awaiting it gives:", result)


if __name__ == "__main__":
    asyncio.run(main())
