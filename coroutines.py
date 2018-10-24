import asyncio
# https://docs.python.org/3/library/asyncio-task.html#id1

async def test():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


if __name__ == "__main__":
    """
    Co-routines declared with async/await syntax is the preferred way of writing asyncio applications. 
    For example, the following snippet of code (requires Python 3.7+) prints “hello”, waits 1 second, and then prints
     “world”:
    """
    asyncio.run(test()) #Call example
    test()  #This will throw "RuntimeWarning: coroutine 'test' was never awaited test()" because you need to apply rhe
    # asyncio.run() method on the async function

    """
    To actually run a coroutine, asyncio provides three main mechanisms:
        - The asyncio.run function to run the top-level entry point in the test() function (see the above example)
        - Awaiting on a co-routine. The following snipped of code will print "hello" after waiting for 1 second, and then 
        print "world" after waiting for another two seconds (example in corutines2.py)
        - The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks. (which is corutines2.py example,
        modified in the coroutines3.py file)
    """