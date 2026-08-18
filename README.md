# List the Topics for Python Async Notes and Code Demonstration
## Basics
- What is Asynchronous Programming
- Synchronous vs Asynchronous vs Multithreading vs Multiprocessing
- The Event Loop
- `async` and `await` Keywords
- Coroutines and Coroutine Functions
- Running a Coroutine (`asyncio.run`)
- Awaitables: Coroutines, Tasks, and Futures
- Creating and Scheduling Tasks (`asyncio.create_task`)
- Sleeping Asynchronously (`asyncio.sleep`)
- Handling Exceptions in Coroutines

## Intermediate
- Running Tasks Concurrently (`asyncio.gather`)
- Waiting for Tasks (`asyncio.wait`, `asyncio.wait_for`)
- Task Cancellation and Timeouts
- Task Groups (`asyncio.TaskGroup`)
- Async Context Managers (`async with`)
- Async Iterators and Async Generators (`async for`)
- Producer-Consumer Pattern with `asyncio.Queue`
- Synchronization Primitives (`Lock`, `Event`, `Condition`, `Semaphore`)
- Async HTTP Requests (`aiohttp`, `httpx`)
- Combining `asyncio` with `concurrent.futures` (Threads/Processes)

## Advanced
- Structured Concurrency Patterns
- Custom Event Loop Policies
- Writing Custom Awaitables and Futures
- Async Context Variables (`contextvars`) and Task-Local State
- Backpressure and Flow Control
- Streams (`asyncio.StreamReader`/`StreamWriter`) for Networking
- Subprocess Management with `asyncio`
- Debugging and Profiling Async Code (`asyncio` debug mode)
- Error Handling and Exception Groups (`asyncio.TaskGroup` + `ExceptionGroup`)
- Performance Considerations and Common Pitfalls (blocking calls, GIL, thread pool sizing)
