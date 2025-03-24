'''
https://leetcode.com/problems/combination-sum/description/

Time Complexity: O(2^t), where t is the target value.

Explanation:

In the worst case, the recursion explores all possible combinations of numbers (including repeated use of the same number) that sum up to the target.

Since each number can be used multiple times, the recursion tree can grow exponentially with respect to the target.

The number of recursive calls is bounded by 2^t in the worst case (though pruning with total > target helps in practice).

The actual time also depends on the size of the result list, since each valid combination is copied into the result.

Space Complexity: O(t)

Explanation:

The maximum depth of the recursion tree is O(t) in the worst case (when repeatedly adding the smallest number until the sum reaches target).

Additionally, space is used to store the result list res, but that depends on the number of valid combinations and is not considered extra space for complexity analysis.
'''

from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in `nums` where the numbers sum to `target`.
        Each number in `nums` can be used an unlimited number of times.
        """
        res = []  # Stores all valid combinations

        def dfs(index: int, current_subset: List[int], total: int):
            """
            Depth-First Search (DFS) helper function to explore combinations.
            :param index: Current index in `nums` to consider.
            :param current_subset: The combination being built.
            :param total: Current sum of elements in `current_subset`.
            """
            # Base case: If the sum reaches the target, store the valid combination
            if total == target:
                res.append(current_subset[:])  # Append a copy to avoid reference issues
                return
            
            # Base case: If out of bounds or sum exceeds target, return
            if index >= len(nums) or total > target:
                return

            # Step 1: Include nums[index] and recurse (can use the same element again)
            current_subset.append(nums[index])  # Choose the current number
            dfs(index, current_subset, total + nums[index])  # Recurse with updated sum

            # Step 2: Exclude nums[index] and move to the next index
            current_subset.pop()  # Undo choice (backtrack)
            dfs(index + 1, current_subset, total)  # Move to next index
        
        # Start the DFS traversal from index 0 with an empty subset and total sum 0
        dfs(0, [], 0)

        return res  # Return the list of valid combinations
