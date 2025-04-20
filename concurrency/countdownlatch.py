'''
🧩 What is a CountDownLatch?
A CountDownLatch allows one or more threads to wait until a set of operations being performed in other threads completes.

You initialize it with a count.

Threads call latch.wait() to wait until the count reaches zero.

Other threads call latch.count_down() to decrement the count.

When count hits zero, all waiting threads proceed.

✅ Why it's more flexible than a Barrier?
A Barrier is resettable and requires a fixed number of parties.

A CountDownLatch:

Can have multiple waiters

Can be counted down from anywhere

Does not reset — it’s a one-shot latch
'''

import threading
import time
import random

class CountDownLatch:
    def __init__(self, count):
        self.count  = count
        self.condition = threading.Condition()

    def wait(self):
        with self.condition:
            while self.count > 0:
                self.condition.wait()

    def count_down(self):
        with self.condition:
            self.count -= 1
            print(f"Latch CountdownL {self.count} remaining")
            if self.count == 0:
                self.condition.notify_all()

def worker(latch: CountDownLatch, thread_id: int):
    print(f"Thread {thread_id} starting work...")
    time.sleep(random.uniform(0.5, 2.0))  # Simulate work
    print(f"Thread {thread_id} finished work. Counting down latch.")
    latch.count_down()

def main():
    num_workers = 3
    latch = CountDownLatch(num_workers)

    for i in range(num_workers):
        threading.Thread(target=worker, args=(latch, i)).start()

    print("[Main Thread] waiting for workers to finish...")
    latch.wait()
    print("[Main Thread] All workers have finished. Proceeding...")

if __name__ == "__main__":
    main()
    print("Main thread finished.")