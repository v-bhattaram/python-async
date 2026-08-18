# Handling Exceptions in Coroutines

Exceptions inside `async def` functions work exactly like normal Python
exceptions — use `try`/`except` around the `await` call.

```python
async def risky():
    raise ValueError("oops")

async def main():
    try:
        await risky()
    except ValueError as e:
        print("caught:", e)
```

## Exceptions inside Tasks
If a coroutine is running as a `Task` (via `asyncio.create_task()`) and it
raises an exception, that exception is stored on the Task and **only
raised when you `await` the task** (or call `task.result()`). If you never
await it, the error is silently swallowed until Python eventually logs a
warning like "Task exception was never retrieved".

```python
task = asyncio.create_task(risky())
await asyncio.sleep(0)  # let it run and fail
# task.exception() is now set, but nothing has crashed yet
try:
    await task           # THIS is where the exception is raised to you
except ValueError as e:
    print("caught:", e)
```

## Files in this folder
- `demo.py` — shows catching an exception from a plain `await` call, and
  catching an exception raised inside a `Task`.

## Run it
```bash
python demo.py
```
