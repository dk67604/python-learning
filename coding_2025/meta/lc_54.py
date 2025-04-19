class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []  # This will store the elements in spiral order
        left, right = 0, len(matrix[0])  # Initialize left and right pointers for columns
        top, bottom = 0, len(matrix)     # Initialize top and bottom pointers for rows

        # Loop until the pointers cross each other
        while left < right and top < bottom:

            # Traverse from left to right on the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # Traverse from top to bottom on the rightmost column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1  # Move the right boundary left

            # Check if we are still within valid boundaries after moving top and right
            if not (left < right and top < bottom):
                break  # If the matrix is fully traversed, exit the loop

            # Traverse from right to left on the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1  # Move the bottom boundary up

            # Traverse from bottom to top on the leftmost column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right

        return res  # Return the spiral order traversal
