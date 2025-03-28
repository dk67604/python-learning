'''
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of the list while maintaining the relative order of the non-zero elements.
        Modifies the input list in-place.
        """
        left = 0  # Position to place the next non-zero element

        # Move all non-zero elements to the front
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
