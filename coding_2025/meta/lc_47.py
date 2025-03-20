'''
https://leetcode.com/problems/permutations-ii/
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []  # Stores all unique permutations
        nums.sort()  # Sorting ensures duplicates are adjacent
        used = [False] * len(nums)  # Track used numbers in the current recursion

        def backtrack(candidates: List[int]):
            # Base case: If current permutation is complete, add it to results
            if len(candidates) == len(nums):
                res.append(candidates[:])  # Append a copy of the current permutation
                return

            # Iterate over the numbers
            for i in range(len(nums)):
                # Skip used numbers
                if used[i]:
                    continue

                # Skip duplicate numbers (only pick the first occurrence in the same recursion level)
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Choose the number
                used[i] = True
                candidates.append(nums[i])

                # Recurse to build the rest of the permutation
                backtrack(candidates)

                # Backtrack: remove the last element and mark it as unused
                candidates.pop()
                used[i] = False

        # Start backtracking with an empty list
        backtrack([])

        return res  # Return all unique permutations
