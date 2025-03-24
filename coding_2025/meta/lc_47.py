'''
https://leetcode.com/problems/permutations-ii/

Time Complexity: O(n × n!) in the worst case, where n is the length of the input list nums.

Explanation:

Without duplicates, the number of permutations is n!, and building each permutation takes O(n) time, giving a total of O(n × n!).

With duplicates, the number of unique permutations is less than n! (depending on how many repeated elements exist), so the actual number of recursive calls is less — but in the worst case (all unique elements), it remains O(n × n!).

Space Complexity: O(n) (excluding the output list)

Explanation:

The recursion stack, used list, and the current candidates list can each grow up to size n.

The result list res is not included in the auxiliary space calculation, but it will take O(n × n!) space to store all permutations in the worst case.
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
