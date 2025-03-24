'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
✅ __init__ Method (Constructor)
Time Complexity: O(m × n)
Where m = number of rows, n = number of columns in the matrix.

You initialize the prefix sum matrix and compute prefix sums row by row.

Each cell is processed exactly once.

Space Complexity: O(m × n)
A new 2D array prefixSum of the same dimensions as the input matrix is created.

✅ sumRegion(row1, col1, row2, col2)
Time Complexity: O(r), where r = row2 - row1 + 1
For each row between row1 and row2, you compute a single subtraction to get the sum for that row segment.

This takes linear time in the number of rows spanned by the region.

⚠️ Note: This is not constant time since the query still loops over rows — it's fast, but not the optimal 2D prefix sum approach (which would be O(1)).

Space Complexity: O(1)
No additional space is used apart from a few variables.
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
