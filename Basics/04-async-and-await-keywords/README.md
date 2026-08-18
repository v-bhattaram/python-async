# `async` and `await` Keywords

- **`async def`** turns a normal function into a **coroutine function**.
  Calling it doesn't run the code immediately — it returns a coroutine
  object that needs to be awaited or scheduled.
- **`await`** can only be used *inside* an `async def` function. It means
  "pause here until this awaitable is done, and let other tasks run
  meanwhile."

```python
async def greet():        # defines a coroutine function
    print("hello")

greet()                   # does NOT print "hello" - just creates a coroutine object
await greet()             # this actually runs it (only works inside async code)
```

## Common mistake
Forgetting `await`:
```python
async def say_hi():
    print("hi")

async def main():
    say_hi()   # BUG: nothing happens (Python warns: "coroutine was never awaited")
    await say_hi()  # correct
```

## Files in this folder
- `demo.py` — shows the difference between calling a coroutine function
  without `await` (nothing happens yet) and with `await` (it actually runs).

## Run it
```bash
python demo.py
```
