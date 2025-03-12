'''
503. Next Greater Element II
Medium
Topics
Companies
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initialize result array with -1, as default values (if no greater element is found)
        res = [-1] * len(nums)
        # Stack to store indices of elements (used for tracking next greater elements)
        stack = []
        
        # First pass: Traverse the array once to fill next greater elements for normal order
        for i, num in enumerate(nums):
            # Check if the current element is greater than the element at the top of the stack
            while stack and nums[stack[-1]] < num:
                # Update result array with next greater element
                res[stack.pop()] = num
            # Push the index onto the stack
            stack.append(i)

        # Second pass: Traverse again to handle the circular nature of the array
        for i, num in enumerate(nums):
            # Process only those elements left in the stack
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num

        return res

