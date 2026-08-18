# The Event Loop

The **event loop** is the engine behind `asyncio`. It's a single loop that:
1. Keeps a list of tasks that are ready to run, or waiting on something
   (a timer, network data, etc.).
2. Runs one task until it hits an `await` and pauses (gives up control).
3. Picks the next ready task and runs it.
4. Repeats, forever, until there's nothing left to do.

Think of it like a **single waiter** in a restaurant who takes an order from
table 1, drops it at the kitchen, then WHILE the kitchen cooks, goes and takes
an order from table 2, then table 3 — instead of standing at table 1 waiting
for the food.

You almost never manage the event loop directly — `asyncio.run()` creates it,
runs your code, and shuts it down for you.

## Event Loop
* Its the Main Tread 
* By `default`, `asyncio.run()` (or `loop.run_forever()`) executes the event loop on whichever thread calls it, which is normally the main thread. The event loop itself is just a loop running on one OS thread; it achieves concurrency by cooperatively switching between coroutines at await points, not by using multiple threads.
* Single-threaded by default: All coroutines, callbacks, and tasks scheduled on a given event loop run sequentially on that one thread. Only one piece of your async code executes at any instant.
* **Not inherently "the main thread"**: asyncio doesn't require the loop to be on the main thread — you can create and run an event loop on a background thread (e.g., threading.Thread(target=loop.run_forever)), which is a common pattern for bridging sync and async code. But unless you do that explicitly, asyncio.run() uses the thread you called it from.
* **Why it feels single-threaded**: Concurrency comes from tasks yielding control (via await) back to the loop, which then runs other ready tasks/callbacks — not from parallel execution on multiple cores.
* **CPU-bound or blocking work** still blocks the whole loop (and thus the thread it's on) unless offloaded via loop.run_in_executor() to a thread/process pool.


## Files in this folder
- `demo.py` — starts three "orders" (coroutines) and prints messages so you
  can see the event loop interleaving them: it doesn't run them one after
  another, it switches between them whenever one pauses at `await`.

## Run it
```bash
python demo.py
```

Watch the output order: `order-1 started` → `order-2 started` →
`order-3 started` all print before any `finished` messages, proving the loop
switched between the tasks instead of running them fully one at a time.
