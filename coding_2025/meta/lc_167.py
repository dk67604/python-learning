'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

🧠 Explanation:
Time Complexity: O(n) — Each pointer moves at most n times (once from each end), so it's linear.

Space Complexity: O(1) — No extra space is used beyond a few variables.

'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Assumes input list `nums` is sorted in non-decreasing order.
        Returns 1-based indices of two numbers that add up to the target.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left, right = 0, len(nums) - 1  # Initialize two pointers

        # Loop until the two pointers meet
        while left < right:
            sumFound = nums[left] + nums[right]

            if sumFound < target:
                left += 1  # Move left pointer right to increase sum
            elif sumFound > target:
                right -= 1  # Move right pointer left to decrease sum
            else:
                # Found the pair; return 1-based indices
                return [left + 1, right + 1]

        # Return default value if no valid pair found
        return [-1, -1]
