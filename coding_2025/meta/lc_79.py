'''
https://leetcode.com/problems/word-search/description/
O(m × n × 4^L) where:
m × n = total number of cells
L = length of the word
Each DFS call can go in 4 directions for each character.
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Returns True if the given `word` exists in the `board`.
        The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically).
        Same cell cannot be used more than once in a word path.
        """
        ROWS, COLS = len(board), len(board[0])  # Dimensions of the board
        path = set()  # Set to track visited cells in the current DFS path
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 4 directions: down, right, up, left

        def dfs(r: int, c: int, i: int) -> bool:
            """
            Performs DFS to match the `i`th character of `word` starting from board[r][c]
            """
            # Base case: all characters matched
            if i == len(word):
                return True

            # Check boundaries, visited, and character mismatch
            if (
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in path or 
                board[r][c] != word[i]
            ):
                return False

            # Mark current cell as visited
            path.add((r, c))

            # Explore all 4 directions
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                if dfs(next_r, next_c, i + 1):
                    return True  # If any path returns True, we're done

            # Backtrack: remove cell from visited path
            path.remove((r, c))
            return False

        # Try starting DFS from every cell in the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # If DFS finds the word, return True
                    return True

        # If no path matched the word
        return False
