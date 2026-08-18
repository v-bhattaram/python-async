# Running a Coroutine (`asyncio.run`)

`asyncio.run(coro)` is the standard **entry point** for an async program.
It does three things:
1. Creates a new event loop.
2. Runs the given coroutine until it completes, returning its result.
3. Closes the event loop.

You should call it **once**, from regular (synchronous) top-level code —
usually in the `if __name__ == "__main__":` block. Everything else that
needs to run concurrently happens *inside* that one call, using `await`,
tasks, or `asyncio.gather`.

```python
async def main():
    return "done"

result = asyncio.run(main())  # blocks here until main() finishes
print(result)                 # "done"
```

## Common mistake
Calling `asyncio.run()` more than once, or calling it from inside another
coroutine — both raise errors or are unnecessary. There should be exactly one
`asyncio.run()` call per program.

## Files in this folder
- `demo.py` — a minimal coroutine started with `asyncio.run()`, showing that
  it returns the coroutine's result.

## Run it
```bash
python demo.py
```
