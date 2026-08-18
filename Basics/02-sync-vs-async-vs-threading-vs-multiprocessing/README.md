# Synchronous vs Asynchronous vs Multithreading vs Multiprocessing

There are four common ways to run work in Python. Each solves a different
problem:

| Style | What runs | Best for | Analogy |
|---|---|---|---|
| **Synchronous** | One thing at a time, in order | Simple scripts | One cashier serving one customer fully, then the next |
| **Asynchronous** (`asyncio`) | One thread, but switches between tasks while they *wait* (e.g. network/disk) | Many I/O-bound tasks (web requests, DB calls) | One cashier serving many customers by working on whoever isn't currently "thinking" |
| **Multithreading** (`threading`) | Multiple threads, same process | I/O-bound tasks, or mixing with blocking libraries | Several cashiers sharing one till, taking turns because of the GIL |
| **Multiprocessing** (`multiprocessing`) | Multiple separate processes | CPU-bound tasks (heavy computation) | Several independent cashiers, each with their own till |

## Why not always use threads/processes?
- Python has a **Global Interpreter Lock (GIL)**: only one thread executes
  Python bytecode at a time, so threads don't help CPU-bound work.
- Processes have real parallelism but cost more memory and startup time.
- `asyncio` has the least overhead for I/O-bound work (no thread/process
  switching), but a single blocking call can freeze the whole event loop.

## Files in this folder
Each script does the **same job** — "wait" 3 times for 1 second each (simulating
I/O) — using a different style, so you can compare:
- `sync_demo.py`
- `async_demo.py`
- `threading_demo.py`
- `multiprocessing_demo.py`

## Run it
```bash
python sync_demo.py
python async_demo.py
python threading_demo.py
python multiprocessing_demo.py
```

Notice `sync_demo.py` takes ~3s, while the other three take ~1s because the
three waits happen concurrently.
