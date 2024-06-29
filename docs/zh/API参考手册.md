# 异步 I/O 调度器 —— uasyncio

uasyncio 是用来编写 **并发** 代码的库，使用 **async/await** 语法。uasyncio 被用作多个提供高性能异步框架的基础，包括网络和网站服务，数据库连接库，分布式任务队列等等。uasyncio 往往是构建 IO 密集型和高层级 **结构化** 网络代码的最佳选择。

## 核心功能

### `uasyncio.create_task(coro)`

>  从给定的协程创建一个新任务并安排它运行。 

**参数**

- `core`：协程对象

**返回值**：相应的`Task`对象

### `uasyncio.run(coro) `

>  从给定的协程创建一个新任务并运行它直到完成 

**参数**

- `coro`：协程对象

**返回值**： 返回coro返回的值。 

### `uasyncio.sleep(t) `

>  睡眠t秒（可以是浮点数）。 这是一个协程。

### `uasyncio.sleep_ms(t)`

>  休眠t毫秒。 这是一个协程。 

## 附加功能

### `uasyncio.wait_for(awaitable, timeout)`

>  等待awaitable完成，但如果它需要更长的超时秒数，请取消它。如果awaitable不是任务，那么将从它创建一个任务。
>
> 如果发生超时，它会取消任务并引发`asyncio.TimeoutError`: ：这应该被调用者捕获。
>
> 返回awaitable的返回值。
>
> 这是一个协程。

**参数**：

- `awaitable`：可等待对象。
- `timeout`：超时时间

**返回值**：返回`awaitable`返回的值。

### `uasyncio.wait_for_ms(awaitable,  timeout)`

> 类似于`wait_for`但超时是以毫秒为单位的整数。
>
> 这是一个协程。

**参数**：

- `awaitable`：可等待对象
- `timeout`：超时时间

**返回值**：返回`awaitable`返回值。

###  `uasyncio.gather(awaitables, return_exceptions=False)`

> 同时运行所有等待。任何不是任务的等待项都被提升为任务。
>
> 返回所有awaitables的返回值列表。
>
> 这是一个协程。

**参数**：

- `awaitable`：可等待对象
- `return_exceptions`：是否返回异常对象标志。

**返回值**：返回`awaitable`返回值。

## 协程事件

### `uasyncio.Event` 

>  创建一个可用于同步任务的新事件。事件以清除状态开始。

###  `Event.is_set()`

>  `True`如果设置了事件，则返回，`False`否则返回。 

###  `Event.set()`

> 设置事件。任何等待事件的任务都将被安排运行。

###  `Event.clear()`

>  清除事件。 

###  `Event.wait()`

> 等待事件被设置。如果事件已经设置，那么它会立即返回。
>
> 这是一个协程。