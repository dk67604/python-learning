'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Time complexity: The time complexityof thefind_the_median_from_two_sorted_arays
 functionis becauseweperformbinarysearchoverthesmallerofthetwoinput 𝑂(𝑙𝑜𝑔(𝑚𝑖𝑛(𝑚,𝑛)))
 arrays.
 Spacecomplexity:Thespacecomplexityis .
'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to perform binary search on it
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # Half of the total number of elements (used to partition the arrays)
        half_total_len = (m + n) // 2

        # Initialize binary search bounds
        left, right = 0, m - 1

        while True:
            # Binary search on nums1: pick middle index
            L1_index = (left + right) // 2
            # L2_index is derived to ensure left part has exactly half_total_len elements
            L2_index = half_total_len - (L1_index + 1) - 1

            # Get left and right values around the partition in nums1
            L1 = float('-inf') if L1_index < 0 else nums1[L1_index]
            R1 = float('inf') if L1_index >= m - 1 else nums1[L1_index + 1]

            # Get left and right values around the partition in nums2
            L2 = float('-inf') if L2_index < 0 else nums2[L2_index]
            R2 = float('inf') if L2_index >= n - 1 else nums2[L2_index + 1]

            # Binary search adjustment: too far right in nums1
            if L1 > R2:
                right = L1_index - 1
            # Too far left in nums1
            elif L2 > R1:
                left = L1_index + 1
            else:
                # Correct partition found
                if (m + n) % 2 == 0:
                    # If total length is even, return average of max of left and min of right
                    return (max(L1, L2) + min(R1, R2)) / 2.0
                else:
                    # If total length is odd, return min of right elements
                    return min(R1, R2)

