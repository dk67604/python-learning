'''
htt
ps://leetcode.com/problems/permutations/description/
Time Complexity: O(n × n!), where n is the number of elements in the input list nums.

Explanation:

There are n! possible permutations of n unique elements.

For each permutation, you build a list of length n, and copying that list to the result takes O(n) time.

Therefore, the total time complexity is O(n × n!).

Space Complexity: O(n) (excluding the output list)

Explanation:

The recursion stack and the candidate list can each grow up to size n.

The used set also holds up to n elements.

The result list res will take O(n × n!) space to store all permutations, but that is typically not counted as auxiliary space.

'''

from typing import List, Set

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the given list of numbers.
        
        :param nums: List of unique integers
        :return: List of all possible permutations
        """
        res = []  # List to store the final permutations
        self.helper(nums, [], set(), res)  # Call the recursive helper function
        return res

    def helper(self, nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
        """
        Recursive helper function to generate permutations using backtracking.
        
        :param nums: Original list of numbers
        :param candidate: Current permutation being built
        :param used: Set to track which numbers are already in `candidate`
        :param res: List to store all valid permutations
        """
        # Base case: If candidate contains all numbers, add a copy to results
        if len(candidate) == len(nums):
            res.append(candidate[:])  # Append a shallow copy to avoid modifications
            return  # Stop further recursion

        # Iterate over all numbers to build permutations
        for num in nums:
            if num not in used:  # Ensure we don’t reuse numbers in the same permutation
                candidate.append(num)  # Choose: Add num to the current permutation
                used.add(num)  # Mark num as used

                self.helper(nums, candidate, used, res)  # Recur with updated candidate

                candidate.pop()  # Undo choice (backtrack)
                used.remove(num)  # Unmark num as used
