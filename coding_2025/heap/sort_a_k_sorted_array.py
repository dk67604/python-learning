'''
✅ Time Complexity:
O(n log k)

Building the initial heap: O(k)

Each of the n insertions and deletions on a heap of size k: O(log k)


'''

import heapq
from typing import List

def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    # A k-sorted array is one where every element is at most k positions away from its correct position

    # Step 1: Initialize a min-heap with the first k+1 elements
    min_heap = nums[:k+1]
    heapq.heapify(min_heap)  # Convert list to a valid min-heap

    insert_index = 0  # Points to the position where the next smallest element should go

    # Step 2: Iterate over the remaining elements in the array
    for i in range(k+1, len(nums)):
        # Pop the smallest from the heap and place it at the correct index in the array
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1
        # Push the current element into the heap
        heapq.heappush(min_heap, nums[i])

    # Step 3: Extract remaining elements from the heap and place them into the array
    while min_heap:
        nums[insert_index] = heapq.heappop(min_heap)
        insert_index += 1

    return nums  # The array is now fully sorted
