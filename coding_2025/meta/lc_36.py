'''
https://leetcode.com/problems/valid-sudoku/

Time Complexity: O(1)

Explanation:

The board size is fixed at 9x9 (standard Sudoku), so the number of iterations is constant: 9 * 9 = 81 cells.

Each check and insertion into a set is done in constant time, O(1).

Since the input size does not grow beyond 81 cells, the entire algorithm runs in constant time.

Space Complexity: O(1)

Explanation:

Although we use sets to store seen values for rows, columns, and subgrids, each can hold at most 9 digits (1–9).

Thus, the total space used is constant and does not scale with input size.
'''

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track the seen digits for each row, column, and 3x3 subgrid
        row_sets = [set() for _ in range(9)]                 # One set per row
        col_sets = [set() for _ in range(9)]                 # One set per column
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]  # 3x3 grid of sets for subgrids

        # Traverse every cell of the board
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # Skip empty cells
                if num == '.':
                    continue

                # Check if number already exists in the current row
                if num in row_sets[r]:
                    return False  # Invalid: duplicate in row

                # Check if number already exists in the current column
                if num in col_sets[c]:
                    return False  # Invalid: duplicate in column

                # Check if number already exists in the current 3x3 subgrid
                if num in subgrid_sets[r // 3][c // 3]:
                    return False  # Invalid: duplicate in subgrid

                # If valid so far, record the number in the appropriate sets
                row_sets[r].add(num)
                col_sets[c].add(num)
                subgrid_sets[r // 3][c // 3].add(num)

        # If we complete the loop with no conflicts, the board is valid
        return True
