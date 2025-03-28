import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Partition function to rearrange elements around a pivot
        def partition(nums: List[int], left: int, right: int) -> int:
            # Choose a random pivot and move it to the end
            pivot_index = random.randint(left, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            pivot = nums[right]
            
            # Pointer for the next smaller-than-pivot position
            lo = left
            for i in range(left, right):
                # Push all smaller elements to the left
                if nums[i] < pivot:
                    nums[lo], nums[i] = nums[i], nums[lo]
                    lo += 1
            
            # Finally place pivot in its correct sorted position
            nums[lo], nums[right] = nums[right], nums[lo]
            return lo  # Return the pivot index

        # Quickselect to find the kth largest element
        def quickselect(nums: List[int], left: int, right: int, k: int) -> int:
            n = len(nums)
            # Base case: only one element
            if left >= right:
                return nums[left]

            # Partition and get pivot index
            pivot_index = partition(nums, left, right)

            # Target index for kth largest is (n - k)
            if pivot_index < n - k:
                # Recurse right
                return quickselect(nums, pivot_index + 1, right, k)
            elif pivot_index > n - k:
                # Recurse left
                return quickselect
