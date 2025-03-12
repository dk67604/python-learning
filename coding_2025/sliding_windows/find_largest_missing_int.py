'''
Find the Largest Almost Missing Integer
Easy
3 pt.
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.
'''

from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        """
        Finds the largest unique integer in any subarray of length `k`.
        
        Approach:
        - Use a sliding window technique to iterate through all subarrays of size `k`.
        - Maintain a frequency map to track occurrences of numbers in subarrays.
        - Identify the largest integer that appears exactly once across all subarrays.

        Time Complexity: O(N * K) in worst case (for small `k`).
        Space Complexity: O(N) for the frequency map.
        """
        
        # Edge case: if k is larger than the list length, return -1
        if k > len(nums):
            return -1
        
        freq_map = {}  # Dictionary to store frequency of elements
        left, right = 0, 0  # Sliding window pointers

        # Step 1: Iterate through the list using a sliding window of size `k`
        while right < len(nums):
            if right - left + 1 == k:  # When window size reaches `k`
                sub_array = nums[left:right+1]  # Extract the subarray
                
                # Count the frequency of elements in the current subarray
                for item in set(sub_array):  # Use set to avoid duplicate counting
                    freq_map[item] = freq_map.get(item, 0) + 1
                
                # Move the left pointer forward to slide the window
                left += 1
            
            right += 1  # Expand the window by moving right pointer
        
        max_res = -1  # Variable to store the maximum unique integer

        # Step 2: Find the largest integer that appears exactly once
        for num, count in freq_map.items():
            if count == 1:  # Only consider numbers appearing once
                max_res = max(num, max_res)
            
        return max_res  # Return the largest unique integer found
