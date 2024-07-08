# 0x01. Python - Async Function
This project covers asynchronous programming in Python using async and await keywords. It is part of the ALX Backend Python curriculum.

## Learning Objectives
* Understand the basics of asynchronous programming in Python.
* Learn how to use async and await to define and work with asynchronous functions.
* Explore the asyncio library for managing asynchronous tasks.
## Requirements
* Python 3.7 or higher.
* Familiarity with basic Python programming.
## Project Structure
The project includes the following files:

* 0-basic_async_syntax.py: Basic syntax of async and await.
* 1-async_comprehension.py: Using async comprehensions.
* 2-measure_runtime.py: Measuring the runtime of asynchronous functions.
* 3-concurrent_coroutines.py: Running multiple coroutines concurrently.
## Usage
To run the examples, make sure you have Python 3.7 or higher installed. You can run each Python file using the command:

```sh
Copy code
python3 filename.py
```
For example:

```sh
Copy code
python3 0-basic_async_syntax.py
```
Examples
0-basic_async_syntax.py
This script demonstrates basic async and await syntax.

```python
Copy code
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```
1-async_comprehension.py
This script shows how to use async comprehensions.
```
python
Copy code
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()

async def async_comprehension():
    return [i async for i in async_generator()]

asyncio.run(async_comprehension())
```
2-measure_runtime.py
This script measures the runtime of asynchronous functions.
```
python
Copy code
import asyncio
import time

async def measure_runtime():
    start = time.perf_counter()
    await asyncio.sleep(1)
    end = time.perf_counter()
    return end - start

runtime = asyncio.run(measure_runtime())
print(f"Runtime: {runtime} seconds")
```
3-concurrent_coroutines.py
This script demonstrates running multiple coroutines concurrently.
```
python
Copy code
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world')
    )

asyncio.run(main())
```
## Author
Efa07 - GitHub
efatariku07@gmail.com
## License
This project is licensed under the MIT License - see the LICENSE file for details.