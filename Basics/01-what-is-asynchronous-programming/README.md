# What is Asynchronous Programming

Asynchronous programming lets a program **start a slow task (like waiting for a
file, a network response, or a timer), and while it waits, go do other useful
work**, instead of just sitting idle (blocking).

Think of a cook in a kitchen:
- **Synchronous (blocking)**: Put water on to boil, stand and stare at the pot
  until it boils, THEN start chopping vegetables.
- **Asynchronous (non-blocking)**: Put water on to boil, and WHILE it boils,
  start chopping vegetables. Come back to the pot when it's ready.

In Python, this is done with the `asyncio` library, using the keywords
`async` and `await`.

## Key idea
- A normal function runs start-to-finish and blocks everything else.
- An `async` function (a "coroutine") can **pause** at `await` points to let
  other code run, then **resume** later.

## Files in this folder
- `demo.py` — compares blocking (synchronous) waiting vs non-blocking
  (asynchronous) waiting for two "tasks" that each take 2 seconds.

## Run it
```bash
python demo.py
```

You'll see the synchronous version take ~4 seconds (2 + 2, one after another)
and the asynchronous version take ~2 seconds (both wait "at the same time").
