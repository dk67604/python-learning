'''
https://leetcode.com/problems/find-peak-element/description/
✅ Time Complexity: O(log n), where n is the number of elements in the input list nums.
Explanation:

The function uses binary search, which reduces the search space by half in each iteration.

So even in the worst case, it performs at most log₂(n) comparisons.

This is much faster than a linear scan (O(n)) and meets the problem’s logarithmic time requirement.

✅ Space Complexity: O(1)
Explanation:

Only a few variables (lo, hi, mid) are used.

No extra space is used that scales with the input size.

🧠 Summary:
Time Complexity: O(log n)

Space Complexity: O(1)
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize the search space with low and high pointers
        lo, hi = 0, len(nums) - 1
        
        # Perform binary search
        while lo < hi:
            mid = (lo + hi) // 2  # Find the middle index
            
            # Compare the mid element with the next element
            if nums[mid] < nums[mid + 1]:
                # If mid is less than mid+1, peak must be on the right side
                lo = mid + 1
            else:
                # If mid is greater than or equal to mid+1, peak must be on the left side (including mid)
                hi = mid
        
        # Since lo and hi converge, return the peak index
        return lo
