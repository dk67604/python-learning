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
