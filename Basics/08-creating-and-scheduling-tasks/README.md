# Creating and Scheduling Tasks (`asyncio.create_task`)

If you just `await` coroutines one after another, they still run one at a
time (in order) — you get no concurrency:

```python
await work("A")  # waits for A to finish...
await work("B")  # ...then starts B
```

`asyncio.create_task(coro)` wraps a coroutine into a **Task** and schedules
it to start running on the event loop **immediately**, without waiting.
This is how you actually get concurrency — start multiple tasks, then await
them later to get their results.

```python
task_a = asyncio.create_task(work("A"))  # starts running right away
task_b = asyncio.create_task(work("B"))  # also starts running right away
await task_a
await task_b
```

## Files in this folder
- `demo.py` — compares plain sequential `await` calls vs using
  `asyncio.create_task()` to run the same two jobs concurrently.

## Run it
```bash
python demo.py
```
