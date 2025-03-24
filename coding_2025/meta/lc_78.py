'''
https://leetcode.com/problems/subsets/description/

Time Complexity: O(2^n), where n is the number of elements in the input list nums.

Explanation:

Each element in the list has two choices: include or exclude.

This results in 2^n total subsets (the size of the power set).

Each subset is constructed in O(n) time (due to copying the list), but since we only copy when reaching the base case, and we have 2^n such cases, the total time complexity is O(2^n).

Space Complexity: O(n) (excluding the output)

Explanation:

The recursion stack and the current subset curr_subset can grow up to size n.

The result list res stores 2^n subsets, but that is not counted as auxiliary space — it's part of the required output.
'''

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of a given list of numbers.
        Uses backtracking to explore both inclusion and exclusion of each element.
        """
        res = []  # Stores all subsets

        def helper(i: int, curr_subset: List[int]):
            """
            Recursive helper function to build subsets.
            :param i: Current index in `nums`
            :param curr_subset: The subset being built in this recursion path
            """
            # Base case: If we reach the end of the list, add the current subset to results
            if i == len(nums):
                res.append(curr_subset[:])  # Append a shallow copy of the subset
                return

            # Step 1: Include nums[i] in the subset
            curr_subset.append(nums[i])  # Add current element
            helper(i + 1, curr_subset)   # Recurse with the next index

            # Step 2: Exclude nums[i] from the subset (backtrack)
            curr_subset.pop()  # Remove last element (undo inclusion)
            helper(i + 1, curr_subset)  # Recurse without the current element
        
        # Start backtracking from index 0 with an empty subset
        helper(0, [])

        return res  # Return the final list of subsets
