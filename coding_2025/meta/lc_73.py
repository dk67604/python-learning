'''
https://leetcode.com/problems/set-matrix-zeroes/description/
'''

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place:
        If any element is 0, sets its entire row and column to 0.
        Uses first row and column as markers to achieve O(1) space.
        """
        m, n = len(matrix), len(matrix[0])

        # Flag to remember if the first row has any zero
        first_row_has_zero = False
        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # Flag to remember if the first column has any zero
        first_col_has_zero = False
        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and first column to mark zeros
        # If matrix[i][j] == 0, mark matrix[i][0] and matrix[0][j] as 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0  # Mark column
                    matrix[i][0] = 0  # Mark row

        # Set elements to 0 based on the markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # If first row originally had a zero, zero out the whole row
        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        # If first column originally had a zero, zero out the whole column
        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0
