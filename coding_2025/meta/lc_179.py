'''
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
from typing import List
from functools import cmp_to_key  # Import for custom sorting comparator

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings for lexicographical comparison
        array = list(map(str, nums))

        # Custom comparator function to determine sorting order
        def compare_num(n1, n2):
            # Compare concatenated numbers: (n1 + n2) vs (n2 + n1)
            if n1 + n2 > n2 + n1:
                return -1  # Place n1 before n2 (higher order)
            else:
                return 1   # Place n2 before n1 (higher order)

        # Sort using the custom comparator (descending order)
        array.sort(key=cmp_to_key(compare_num))

        # Edge case: If the largest number is "0", return "0" instead of "000..."
        if array[0] == "0":
            return "0"

        # Join the sorted elements to form the largest possible number
        largest = ''.join(array)

        return largest
