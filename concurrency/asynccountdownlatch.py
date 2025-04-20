import asyncio

class AsyncCountDownLatch:
    def __init__(self, count: int):
        self._count = count
        self._condition = asyncio.Condition()

    async def count_down(self):
        async with self._condition:
            self._count -= 1
            print(f"Latch Countdown {self._count} remaining")
            if self._count == 0:
                self._condition.notify_all()

    async def wait(self):
        async with self._condition:
            while self._count > 0:
                await self._condition.wait()

import random

async def async_worker(latch: AsyncCountDownLatch, worker_id: int):
    print(f"Worker-{worker_id} starting setup...")
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate setup time
    print(f"Worker-{worker_id} finished setup. Counting down latch.")
    await latch.count_down()


async def main():
    num_workers = 4
    latch = AsyncCountDownLatch(num_workers)

    tasks = [asyncio.create_task(async_worker(latch, i)) for i in range(num_workers)]

    print("[Main Thread] waiting for workers to finish setup...")
    await latch.wait()
    print("[Main Thread] All workers have finished setup. Proceeding...")
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    print("Main thread finished.")