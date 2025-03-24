'''
https://leetcode.com/problems/3sum/description/

Time Complexity: O(n^2), where n is the number of elements in the input list nums.

Explanation:

First, the array is sorted in O(n log n) time.

Then, the algorithm uses a loop to fix one element and applies the two-pointer approach for the remaining two elements.

For each element, the two-pointer traversal takes O(n) time in the worst case, and this happens for n elements.

Hence, the overall time complexity is O(n^2).

Space Complexity: O(1) (excluding the output list).

The algorithm does not use any extra space for computation; it modifies pointers in-place after sorting.

However, the space required for the result list depends on the number of valid triplets found, which can vary based on the input.
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array `nums`, return all unique triplets [nums[i], nums[j], nums[k]]
        such that `nums[i] + nums[j] + nums[k] == 0`.
        """

        nums.sort()  # Step 1: Sort the array to allow two-pointer traversal
        res = []  # Stores the final list of unique triplets

        # Step 2: Iterate through the sorted list to find triplets
        for i, a in enumerate(nums):
            # Optimization: Since `nums` is sorted, if `nums[i] > 0`, no triplet can sum to zero.
            if a > 0:
                break  # No valid triplet exists beyond this point.

            # Skip duplicate values to avoid duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue  # Skip processing the same number again

            # Step 3: Two-pointer approach to find pairs that sum to `-a`
            l, r = i + 1, len(nums) - 1  # Left and right pointers

            while l < r:
                threeSum = a + nums[l] + nums[r]  # Calculate sum of triplet
                
                if threeSum > 0:
                    r -= 1  # Move the right pointer left to decrease the sum
                elif threeSum < 0:
                    l += 1  # Move the left pointer right to increase the sum
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])

                    # Move left pointer forward while skipping duplicate values
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  # Skip duplicate numbers to ensure unique triplets

        return res  # Return the list of unique triplets
