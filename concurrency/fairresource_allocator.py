import heapq
import itertools
import threading
from collections import defaultdict, deque

class FairPriorityAllocator:
    def __init__(self, max_slots) -> None:
        self.max_slots = max_slots
        self.available_slots = max_slots
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.wait_heap = []
        self.counter = itertools.count()

    def acquire_resource(self, thread_id, priority):
        with self.condition:
            counter = next(self.counter)
            entry = (priority, counter, thread_id)
            heapq.heappush(self.wait_heap, entry)

            while self.wait_heap[0][2] != thread_id or self.available_slots == 0:
                self.condition.wait()

            heapq.heappop(self.wait_heap)
            self.available_slots -= 1
            print(f"[ACQUIRE] Thread {thread_id} with priority {priority} acquired. Available: {self.available_slots}")

    def release_resource(self, thread_id):
        with self.condition:
            self.available_slots += 1
            print(f"[RELEASE] Thread {thread_id} released. Available: {self.available_slots}")
            self.condition.notify_all()

import time
import random

allocator = FairPriorityAllocator(max_slots=2)
log = []

def thread_task(thread_id, priority):
    allocator.acquire_resource(thread_id, priority)
    log.append(f"{thread_id} started with priority {priority}")
    time.sleep(random.uniform(0.5, 1.0))  # Simulate resource usage
    allocator.release_resource(thread_id)
    log.append(f"{thread_id} finished")

# Simulate 6 threads with mixed priorities
threads = []
priorities = [2, 1, 3, 1, 2, 0]  # Lower number = higher priority
for i in range(6):
    t = threading.Thread(target=thread_task, args=(f"T{i}", priorities[i]))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()

print(log)
