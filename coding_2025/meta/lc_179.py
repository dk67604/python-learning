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

✅ Time Complexity: O(n log n * k)
Where:

n = number of elements in nums

k = average length of the numbers (as strings)

Explanation:
String conversion of each number takes O(n * k), where k is the average digit length of the numbers.

Sorting takes O(n log n) comparisons.

Each comparison involves concatenating two strings (n1 + n2 and n2 + n1), which takes O(k) time.

So total sorting complexity is O(n log n * k)

Joining the strings at the end takes O(n * k) time.

So overall, the dominant term is O(n log n * k) due to the custom sort.

✅ Space Complexity: O(n * k)
Explanation:

You store all numbers as strings → O(n * k) space.

The sorted array and final joined string also take O(n * k) space.

🧠 Summary:
Time Complexity: O(n log n * k)

Space Complexity: O(n * k)
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
