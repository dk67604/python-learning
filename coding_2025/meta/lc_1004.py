'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the longest contiguous subarray that contains only 1s
        after flipping at most `k` 0s.

        :param nums: List of binary integers (0s and 1s)
        :param k: Maximum number of 0s that can be flipped
        :return: Length of the longest contiguous subarray with at most k flips
        """
        
        left = 0  # Left pointer for the sliding window
        
        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1  # Use one of the available flips
            
            # If k goes below 0, it means we have used more than allowed flips
            if k < 0:
                # If the left pointer is at a zero, recover one flip when moving past it
                if nums[left] == 0:
                    k += 1  
                left += 1  # Move the left pointer forward to reduce the window size
        
        # The length of the longest valid subarray is (right - left + 1)
        return right - left + 1
