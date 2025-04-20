import multiprocessing
import heapq
import random

def process_chunk_with_queue(chunk, k, queue):
    max_heap = []
    for num in chunk:
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    queue.put(max_heap)
    print(f"Process {multiprocessing.current_process().name} finished processing chunk.")

def kth_smallest_multiprocessing(nums, k, num_processes=4):
    chunk_size = len(nums) // num_processes
    processes = []
    queue = multiprocessing.Queue()
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else len(nums)
        chunk = nums[start:end]
        p = multiprocessing.Process(target=process_chunk_with_queue, args=(chunk, k, queue))
        processes.append(p)
        p.start()
        print(f"Process {p.name} started processing chunk: {chunk}")

    for p in processes:
        p.join()

    final_heap = []
    for _ in range(num_processes):
        local_heap = queue.get()
        for num in local_heap:
            heapq.heappush(final_heap, num)
            if len(final_heap) > k:
                heapq.heappop(final_heap)
    return -final_heap[0] if final_heap else None
if __name__ == "__main__":
    nums =[random.randint(100, 500) for _ in range(50)]
    print(f"Input numbers: {nums}")
    k = 3
    result = kth_smallest_multiprocessing(nums, k)
    print(f"The {k}th smallest element is: {result}")