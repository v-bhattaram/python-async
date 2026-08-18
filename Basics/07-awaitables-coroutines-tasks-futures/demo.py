"""Three kinds of awaitables: coroutine, Task, and Future."""
import asyncio


async def say(msg):
    await asyncio.sleep(0.5)
    return msg


async def main():
    # 1. Coroutine: plain result of calling an async def function
    coro_result = await say("hello from a coroutine")
    print(coro_result)

    # 2. Task: schedules the coroutine to start running right away
    task = asyncio.create_task(say("hello from a task"))
    task_result = await task
    print(task_result)

    # 3. Future: a bare "box" for a result, filled in manually
    future = asyncio.Future()
    future.set_result("hello from a future")
    future_result = await future
    print(future_result)


if __name__ == "__main__":
    asyncio.run(main())
