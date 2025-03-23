'''
https://leetcode.com/problems/valid-sudoku/
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
