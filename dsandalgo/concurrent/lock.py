"""
A lock is a simple synchronization mechanism used to ensure that only one thread or process can access a shared resource at a time.

How it works:

A lock can be in one of two states: locked or unlocked.
When a thread acquires a lock, it sets the lock to the locked state. If another thread tries to acquire the same lock while it's locked, it will be blocked until the lock is released.
Once the thread that holds the lock finishes its operation, it releases the lock, allowing another waiting thread to acquire it.
Use case:

Locks are used to protect critical sections of code where shared resources are accessed or modified, preventing race conditions.


"""

import threading

lock = threading.Lock()
def critical_section():
    lock.acquire()
    try:
          print(f"{threading.current_thread().name} is in the critical section")
    finally:
        lock.release()

threads = [threading.Thread(target=critical_section) for _ in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()
