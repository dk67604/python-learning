'''
https://leetcode.com/problems/combination-sum-ii/description/

Time Complexity: O(2^n), where n is the number of elements in the candidates list.

Explanation:

The solution uses backtracking to explore all subsets of the input list.

In the worst case, each number has two choices: include or exclude, leading to 2^n possible combinations.

Sorting the list takes O(n log n), but the dominant term is the recursive exploration.

Due to the pruning (if cur + candidates[i] > target) and skipping of duplicates, the actual number of recursive calls is much smaller in practice, but still exponential in the worst case.

Space Complexity: O(n)

Explanation:

The recursion stack can go as deep as n in the worst case (when building a long combination).

Aside from the result list res (which is not counted in auxiliary space), only the path list and recursion call stack contribute to space usage.

'''

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of `candidates` where the numbers sum to `target`.
        Each number in `candidates` can only be used once in a combination.
        """

        res = []  # Stores all valid unique combinations
        candidates.sort()  # Step 1: Sort the input array to handle duplicates efficiently

        def dfs(idx: int, path: List[int], cur: int):
            """
            Depth-First Search (DFS) helper function to explore combinations.
            :param idx: Current index in `candidates` to consider.
            :param path: The current combination being built.
            :param cur: The current sum of elements in `path`.
            """
            # Base case: If the sum reaches the target, store the valid combination
            if cur == target:
                res.append(path[:])  # Append a copy to avoid reference issues
                return

            # Step 2: Iterate through the candidates, starting from `idx`
            for i in range(idx, len(candidates)):
                # Step 3: Skip duplicate numbers (to avoid duplicate combinations)
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicate elements at the same recursion level
                
                # Step 4: Prune the search if the sum exceeds the target
                if cur + candidates[i] > target:
                    break  # Since `candidates` is sorted, all further values will also be too large
                
                # Step 5: Include `candidates[i]` in the combination and recurse
                path.append(candidates[i])  # Choose the current element
                dfs(i + 1, path, cur + candidates[i])  # Move to the next index (no reuse allowed)

                # Step 6: Backtrack - Remove the last element to explore other possibilities
                path.pop()

        # Start DFS traversal from index 0 with an empty subset and sum 0
        dfs(0, [], 0)

        return res  # Return the list of unique valid combinations
