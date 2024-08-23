"""
A semaphore is a more general synchronization primitive that can control access to a resource pool, allowing multiple threads or processes to access the resource concurrently up to a certain limit.

How it works:

A semaphore maintains a counter representing the number of permits available. When a thread acquires the semaphore, it decreases the counter. If the counter is zero, the thread is blocked until another thread releases the semaphore (increasing the counter).
Semaphores can be binary (similar to a lock or mutex with a counter of 1) or counting semaphores that allow multiple threads to acquire the resource concurrently up to a certain limit.
Use case:

Semaphores are used when you have a limited number of identical resources, and you need to control how many threads can access those resources simultaneously (e.g., a pool of database connections or a fixed number of worker threads).
"""
import threading
import time

semaphore = threading.Semaphore(2)  # Only 2 threads can access the resource at a time

def limited_access():
    with semaphore:
        print(f"{threading.current_thread().name} is accessing the resource")
        time.sleep(2)
        print(f"{threading.current_thread().name} is releasing the resource")

threads = [threading.Thread(target=limited_access) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()