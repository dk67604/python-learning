from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Finds the longest increasing path in a matrix where adjacent cells 
        can only be part of the path if they contain strictly increasing values.

        Uses Depth-First Search (DFS) with Memoization (Top-Down DP).

        :param matrix: 2D list of integers
        :return: Length of the longest increasing path
        """
        
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])  # Get matrix dimensions
        memo = [[0] * n for _ in range(m)]  # Memoization table

        def dfs(r: int, c: int) -> int:
            """
            Depth-First Search (DFS) to find the longest increasing path from (r, c).
            Uses memoization to store already computed paths.

            :param r: Row index
            :param c: Column index
            :return: Length of the longest increasing path starting from (r, c)
            """
            if memo[r][c] != 0:  # If already computed, return the stored result
                return memo[r][c]

            max_path = 1  # Minimum path length is 1 (the cell itself)
            
            # Directions: Down, Right, Up, Left
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for dr, dc in directions:
                next_r, next_c = r + dr, c + dc
                
                # Check if next position is valid and has a greater value
                if 0 <= next_r < m and 0 <= next_c < n and matrix[next_r][next_c] > matrix[r][c]:
                    max_path = max(max_path, 1 + dfs(next_r, next_c))  # Recursive DFS call

            memo[r][c] = max_path  # Store result in memoization table
            return max_path  # Return computed max path length

        # Compute longest increasing path for each cell
        return max(dfs(r, c) for r in range(m) for c in range(n))
