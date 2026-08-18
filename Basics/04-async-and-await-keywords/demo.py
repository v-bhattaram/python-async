"""async creates a coroutine, await actually runs it."""
import asyncio


async def say_hi():
    print("hi!")


async def main():
    print("Calling say_hi() WITHOUT await:")
    coro = say_hi()          # just creates a coroutine object, does not run it
    print(f"  -> got back: {coro!r} (nothing printed above, code hasn't run yet)")
    coro.close()             # avoid the "never awaited" warning

    print("Calling say_hi() WITH await:")
    await say_hi()            # now it actually runs


if __name__ == "__main__":
    asyncio.run(main())
