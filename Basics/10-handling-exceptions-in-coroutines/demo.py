"""Catching exceptions raised inside coroutines and Tasks."""
import asyncio


async def risky(fail):
    await asyncio.sleep(0.1)
    if fail:
        raise ValueError("something went wrong")
    return "all good"


async def main():
    # 1. Exception from a plain await call
    print("Direct await:")
    try:
        await risky(fail=True)
    except ValueError as e:
        print("  caught:", e)

    # 2. Exception raised inside a Task, only surfaces when awaited
    print("Task-based:")
    task = asyncio.create_task(risky(fail=True))
    await asyncio.sleep(0.2)  # give the task time to run and fail
    print("  task failed already, but no crash yet")
    try:
        await task  # re-raises the stored exception here
    except ValueError as e:
        print("  caught from task:", e)

    # 3. A successful case, for contrast
    result = await risky(fail=False)
    print("Success case:", result)


if __name__ == "__main__":
    asyncio.run(main())
