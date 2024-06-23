import asyncio

def async_decorator(func):
    async def wrapper(*args, **kwargs):
        # Perform async setup tasks
        await asyncio.sleep(1)
        print("Async setup completed.")
        
        # Call the original function
        result = await func(*args, **kwargs)
        
        # Perform async teardown tasks
        await asyncio.sleep(1)
        print("Async teardown completed.")
        
        return result
    
    return wrapper

@async_decorator
async def async_function():
    # Simulate an async task
    await asyncio.sleep(1)
    print("Async task completed.")
    return "Result"

async def main():
    result = await async_function()
    print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
