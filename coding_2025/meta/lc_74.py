'''
https://leetcode.com/problems/search-a-2d-matrix/description/
Time complexity: The time complexity of matrix_search is
 binary searchoverasearchspaceofsize
 𝑚 · 𝑛
 Spacecomplexity:Thespacecomplexityis
 .
 𝑂(1)
 .
 𝑂(𝑙𝑜𝑔(𝑚 · 𝑛))
 becauseitperformsa
'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get matrix dimensions
        m, n = len(matrix), len(matrix[0])
        
        # Apply binary search on the virtual 1D array from index 0 to m*n - 1
        left, right = 0, m * n - 1
        
        while left <= right:
            # Mid index in the virtual 1D array
            mid = (left + right) // 2

            # Convert 1D index to 2D row and column
            r, c = mid // n, mid % n

            # Check the target value at the calculated position
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                # Target is in the left half
                right = mid - 1
            else:
                # Target is in the right half
                left = mid + 1
        
        # Target not found
        return False
