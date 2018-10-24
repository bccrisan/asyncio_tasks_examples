import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# needs debug, no info showed
# async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print('started at', time.strftime('%X'))

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print('finished at', time.strftime('%X'))