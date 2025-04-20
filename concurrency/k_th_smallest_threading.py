import threading
import heapq
import random

def process_chunk(chunk, k, results, index):
    max_heap = []
    for num in chunk:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    results[index] = max_heap
    print(f"Thread {index} finished processing chunk.")

def kth_smallest_threaded(nums, k, num_threads = 4):
    chunk_size = len(nums) // num_threads
    threads = []
    # Initialize list to store max heap results from each thread
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(nums)
        chunk = nums[start:end]
        t = threading.Thread(target=process_chunk, args=(chunk, k, results, i))
        threads.append(t)
        t.start()
        print(f"Thread {i} started processing chunk: {chunk}")

    for t in threads:
        t.join() # Wait for all threads to finish
        print(f"Thread {threads.index(t)} joined.")
        print(f"Thread {threads.index(t)} has finished.")
        print(f"Thread {threads.index(t)} has finished processing chunk.")

    final_heap = []
    for heap in results:
        if heap is not None:  # Check if the heap is not None before iterating
            for num in heap:
                heapq.heappush(final_heap, num)
                if (len(final_heap) > k):
                    heapq.heappop(final_heap)
    return -final_heap[0] if final_heap else None

if __name__ == "__main__":
    nums =[random.randint(100, 500) for _ in range(50)]
    k = 3
    result = kth_smallest_threaded(nums, k)
    print(f"The {k}th smallest element is: {result}")