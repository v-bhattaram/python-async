# Coroutines and Coroutine Functions

- A **coroutine function** is any function defined with `async def`.
- Calling a coroutine function does not run it — it creates a
  **coroutine object** (a paused, resumable computation).
- The coroutine only actually executes when it's `await`-ed, or scheduled
  as a `Task` (see [08-creating-and-scheduling-tasks](../08-creating-and-scheduling-tasks)).

```python
async def add(a, b):     # coroutine function
    return a + b

result = add(1, 2)       # `result` is a coroutine object, NOT 3
```

You can inspect this yourself with `asyncio.iscoroutinefunction()` and
`asyncio.iscoroutine()`.

## Files in this folder
- `demo.py` — defines a coroutine function, shows what calling it produces,
  and then awaits it to get the real result.

## Run it
```bash
python demo.py
```
