# Sleeping Asynchronously (`asyncio.sleep`)

`asyncio.sleep(seconds)` pauses the **current coroutine** for the given
time, without blocking the whole program — the event loop is free to run
other tasks during that time.

This is different from `time.sleep(seconds)`, which blocks **everything**,
including other async tasks.

```python
await asyncio.sleep(1)   # good: only pauses this task
time.sleep(1)             # bad in async code: freezes the entire event loop
```

`asyncio.sleep()` is mostly used in examples/tests to simulate waiting for
something slow (like a network call). In real code, that waiting usually
comes from an actual async library call (e.g. an async HTTP client).

## Files in this folder
- `demo.py` — shows how using `time.sleep()` inside an async task blocks
  everyone else, while `asyncio.sleep()` lets other tasks keep running.

## Run it
```bash
python demo.py
```
