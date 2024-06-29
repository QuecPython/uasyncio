# Asynchronous I/O -- uasyncio

asyncio is a library to write **concurrent** code using the **async/await** syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level **structured** network code.

## Primary Functions

### `uasyncio.create_task(coro)`

>  Create a new task from the given protocol and schedule it to run.

**Params**

- `core`: Coroutine object

**Return value**: Task object

### `uasyncio.run(coro) `

>  Create a new task from the given coroutine and run it until it is completed.

**Params**

- `coro`: Coroutine object

**Return value**: the value of `coro` returns.

### `uasyncio.sleep(t) `

>  Sleep for t seconds (can be a floating-point number). This is a Coroutine.

### `uasyncio.sleep_ms(t)`

>  Sleep for t  milliseconds. This is a Coroutine. 

## Additional Functions

### `uasyncio.wait_for(awaitable, timeout)`

>  Wait for `awaitable` to complete, but if it requires a longer timeout seconds, please cancel it. If awaitable is not a task, then a task will be created from it.
>
> If a timeout occurs, it will cancel the task and trigger ` asyncio.TimeoutError`: This should be captured by the caller.
>
> This is a Coroutine.

**Params**：

- `awaitable`：awaitable object.
- `timeout`：timeout seconds

**Return value**：the value of `awaitable` returns.

### `uasyncio.wait_for_ms(awaitable, timeout)`

> like `wait_for` but the timeout unit is milliseconds.
>
> This is a Coroutine.

**Params**：

- `awaitable`：awaitable object.
- `timeout`：timeout milliseconds

**Return value**：the value of `awaitable` returns.

###  `uasyncio.gather(awaitables, return_exceptions=False)`

> Run all waits simultaneously. Any waiting item that is not a task is elevated to a task.
>
> This is a Coroutine.

**Params**：

- `awaitable`：awaitable object.
- `return_exceptions`: if the exception object returned flag. 

**Return value**：the value of `awaitable` returns.

## Event

### `uasyncio.Event` 

>  Create a new event that can be used to synchronize tasks. The event starts with a clear state.

###  `Event.is_set()`

> `True` returns if an event is set, otherwise `False` returns.

###  `Event.set()`

> Set events. Any task waiting for an event will be scheduled to run.

###  `Event.clear()`

>  clear event.

###  `Event.wait()`

> Wait for the event to be set. If the event has already been set, it will immediately return.
>
> This is a Coroutine.

