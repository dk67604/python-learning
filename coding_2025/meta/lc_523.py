'''
https://leetcode.com/problems/continuous-subarray-sum/description/
'''
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of a remainder
        remainder = {0: -1}  # Initialize with remainder 0 at index -1 to handle edge cases where first element itself is multiple of k
        total = 0  # Variable to maintain the cumulative sum

        # Iterate through the array
        for i, n in enumerate(nums):
            total += n  # Update cumulative sum
            
            # Compute remainder of total sum when divided by k
            r = total % k

            # If this remainder has never been seen before, store the index
            if r not in remainder:
                remainder[r] = i  # Store first occurrence of this remainder
            
            # If we have seen this remainder before and the subarray size is at least 2
            if i - remainder[r] > 1:
                return True  # Found a valid subarray
            
        # If no valid subarray found, return False
        return False
