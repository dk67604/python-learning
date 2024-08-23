import asyncio
import random

class Aggregator:
    def __init__(self) -> None:
        self.total_temperature = 0
        self.reading_count = 0

    async def consume(self, queue: asyncio.Queue):
        while True:
            temperature = await queue.get()
            self.total_temperature += temperature
            self.reading_count +=1
            average_temperature = self.total_temperature / self.reading_count
            print(f"Avg Temp: {average_temperature:.2f}°C after {self.reading_count} readings")
            queue.task_done()

class Sensor:
    async def produce(self, queue: asyncio.Queue):
        for _ in range(5):
            temperature = random.uniform(20, 30)
            print(f"Sensor produced: {temperature:.2f}°C")
            await queue.put(temperature)
            await asyncio.sleep(random.uniform(0.5, 1.5))

async def main():
    queue = asyncio.Queue()
    aggregator = Aggregator()
    sensor = Sensor()

    producer_task = asyncio.create_task(sensor.produce(queue))
    consumer_task = asyncio.create_task(aggregator.consume(queue))

    await producer_task

    await queue.join()

    consumer_task.cancel()

asyncio.run(main())