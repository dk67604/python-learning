import asyncio

async def producer(queue):
    for i in range(5):
        print(f"Producing item {i}")
        await queue.put(i)
        await asyncio.sleep(1)  # Simulate a delay in producing items

async def consumer(queue):
    while True:
        item = await queue.get()  # Non-blocking, waits for an item if queue is empty
        print(f"Consuming item {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=3)

    # Start the producer and consumer
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    # Wait for the producer to finish
    await producer_task

    # Wait for the queue to be fully processed
    await queue.join()

    # Cancel the consumer task as we are done
    consumer_task.cancel()

# Run the event loop
asyncio.run(main())
