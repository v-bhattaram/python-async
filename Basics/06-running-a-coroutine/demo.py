"""asyncio.run() is the single entry point that starts the event loop."""
import asyncio


async def main():
    print("main() started")
    await asyncio.sleep(1)
    print("main() finished")
    return "done"


if __name__ == "__main__":
    result = asyncio.run(main())  # creates loop, runs main(), closes loop
    print("asyncio.run() returned:", result)
