# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, row: int, col: int) -> int:
#     def dimensions(self) -> list[]:
'''
✅ Time Complexity of leftMostColumnWithOne:
Let’s define:

m = number of rows in the binary matrix

n = number of columns in the binary matrix

⏱ Time Complexity: O(m * log n)
For each row (total m rows), the algorithm performs a binary search over the columns (n columns).

Binary search on n columns takes O(log n) time.

Thus, total time = m * O(log n) = O(m log n)

🧠 Space Complexity: O(1)
No extra space is used apart from a few variables (constant space).

'''

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()  # Get matrix dimensions
        smallest_index = cols  # Initialize to maximum possible column index
        
        for row in range(rows):
            lo = 0
            hi = cols - 1
            
            # Binary search for the leftmost 1 in the current row
            while lo <= hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1  # Search in the right half
                else:
                    hi = mid - 1  # Search in the left half
            
            # If a 1 is found, update smallest_index
            if lo < cols and binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        
        # If smallest_index remains unchanged, no 1 was found
        return -1 if smallest_index == cols else smallest_index
