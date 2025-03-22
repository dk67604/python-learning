'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
Time Complexity: O(m)
Space Complexity: O(m * n)
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        
        # Step 1: Initialize a 2D prefix sum matrix with the same dimensions
        self.prefixSum = [[0] * self.COLS for _ in range(self.ROWS)]

        # Step 2: Build row-wise prefix sums
        for row in range(self.ROWS):
            self.prefixSum[row][0] = matrix[row][0]  # First column is the same
            for col in range(1, self.COLS):
                # Add current matrix value to the running row sum
                self.prefixSum[row][col] = self.prefixSum[row][col - 1] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Compute the sum of elements within the rectangle from (row1, col1) to (row2, col2), inclusive.
        Only row-wise prefix sums are used, so each row is processed individually.
        """
        res = 0
        for row in range(row1, row2 + 1):  # Traverse from row1 to row2 inclusive
            if col1 > 0:
                # Use prefix sum: subtract left part (before col1)
                res += self.prefixSum[row][col2] - self.prefixSum[row][col1 - 1]
            else:
                # Start from beginning of row
                res += self.prefixSum[row][col2]

        return res
