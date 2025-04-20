import threading
import time
import random

def worker(barrier: threading.Barrier, thread_id: int):
    print(f"Thread {thread_id} starting setup...")
    time.sleep(random.uniform(0.1, 1.0))  # Simulate setup time
    print(f"Thread {thread_id} finished setup. Waiting at barrier.")

    barrier.wait()  # <-- block until all threads reach here

    print(f"Thread {thread_id} proceeding with main task 🚀")

def main():
    num_threads = 5
    barrier = threading.Barrier(num_threads)

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(barrier, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("All threads have passed the barrier and finished.")

if __name__ == "__main__":
    main()
