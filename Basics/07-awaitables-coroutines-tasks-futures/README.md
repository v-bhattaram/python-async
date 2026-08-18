# Awaitables: Coroutines, Tasks, and Futures

Anything you can put after `await` is called an **awaitable**. There are
three kinds:

1. **Coroutine** — the result of calling an `async def` function.
   Runs only when awaited/scheduled.
2. **Task** — a coroutine wrapped by `asyncio.create_task()`. It starts
   running in the background immediately (scheduled on the event loop),
   even before you `await` it. See
   [08-creating-and-scheduling-tasks](../08-creating-and-scheduling-tasks).
3. **Future** — a low-level "promise" of a result that isn't ready yet.
   You rarely create these yourself; a `Task` *is* a special kind of
   `Future` that runs a coroutine. Libraries use Futures to bridge
   callback-based code with `async`/`await`.

```python
coro = my_coroutine()          # coroutine: not running yet
task = asyncio.create_task(my_coroutine())  # Task: already scheduled/running
future = asyncio.Future()      # Future: an empty box for a result, filled in later
```

## Files in this folder
- `demo.py` — awaits all three kinds of awaitables: a plain coroutine, a
  `Task`, and a manually completed `Future`.

## Run it
```bash
python demo.py
```
