'''
🔧 Problem 2: Thread-Safe Statistics Collector
✅ Problem Statement:
You’re building a concurrent statistics collector that gathers latency values (or any float data) from multiple threads.

Each worker thread reports latency measurements by calling collector.record(value).

At any time, the main thread may call:

collector.mean()

collector.min()

collector.max()

collector.count()

All of these must be thread-safe.

✨ Key Requirements:
Use threading.Lock to guard shared state.

Ensure atomic updates and reads.

Don't use queue or any external libs for state tracking.

🧪 Sample Output:
python
Copy
Edit
collector.record(10)
collector.record(20)
collector.record(15)

collector.count()  # 3
collector.min()    # 10
collector.max()    # 20
collector.mean()   # 15.0
🧠 Concepts Tested:
Thread-safe counters and aggregates

Use of threading.Lock

Coordinated reads/writes

'''
import threading
import time
from typing import List, Optional
import random
import bisect
from collections import defaultdict
class LatencyCollector:

    def __init__(self, bucket_size) -> None:
        self.lock = threading.Lock()
        self.total = 0.0
        self.count_val = 0
        self.min_val = float('inf')
        self.max_val = float('-inf')
        self.latencies = []
        self.hist = defaultdict(int)
        self.bucket_size = bucket_size


    def record(self, value: float):
        with self.lock:
            self.total += value
            self.count_val +=1
            self.min_val = min(self.min_val, value)
            self.max_val = max(self.max_val, value)
            bisect.insort(self.latencies, value) # keep latencies sorted for fast percentile calculation
            bucket_index = int(value // self.bucket_size) * self.bucket_size
            self.hist[bucket_index] += 1

    def mean(self) -> float:
        with self.lock:
            if self.count_val == 0:
                return 0.0
            return self.total / self.count_val

    def min(self) -> Optional[float]:
        with self.lock:
            return self.min_val if self.count_val > 0 else None

    def max(self) -> Optional[float]:
        with self.lock:
            return self.max_val if self.count_val > 0 else None

    def count(self) -> int:
        with self.lock:
            return self.count_val

    def percentile(self, p: float):
        with self.lock:
            if not self.latencies:
                return None

            idx =int( p / 100 * len(self.latencies))
            idx = min(idx, len(self.latencies) - 1)
            return self.latencies[idx]

    def histogram(self):
        with self.lock:
            return dict(sorted(self.hist.items()))


def worker(collector: LatencyCollector):

    for _ in range(5):
        latency = random.uniform(1, 100)
        collector.record(latency)
        time.sleep(0.01)

def main():
    collector = LatencyCollector(bucket_size=20)
    threads = []

    for _ in range(5):
        t = threading.Thread(target=worker, args=(collector,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Total Count: {collector.count()}")
    print(f"Mean: {collector.mean():.2f}")
    print(f"Min: {collector.min():.2f}")
    print(f"Max: {collector.max():.2f}")
    print(f"90th Percentile: {collector.percentile(90):.2f}")
    print("Histogram buckets:")
    for b, count in collector.histogram().items():
        print((f" {b}-{b+19}: {count}"))

if __name__ == "__main__":
    main()