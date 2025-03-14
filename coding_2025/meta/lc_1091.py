from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        
        # Possible 8-directional moves (up, down, left, right, diagonals)
        directions = [(-1,-1), (-1,0), (1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1)]

        # Function to get valid neighbors for BFS traversal
        def get_neighbors(row, col):
            for row_d, col_d in directions:
                new_row = row + row_d
                new_col = col + col_d
                
                # Check if the new position is within bounds
                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                
                # Skip if the cell is blocked (not zero)
                if grid[new_row][new_col] != 0:
                    continue
                
                # Yield valid neighbor coordinates
                yield (new_row, new_col)

        # If the starting or ending cell is blocked, return -1 (no valid path)
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1

        # Initialize a queue for BFS (row, col)
        queue = deque()
        queue.append((0, 0))
        
        # Mark the starting point as visited with distance 1
        grid[0][0] = 1

        # Perform BFS traversal
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]  # Get the current distance from start
            
            # If we reached the bottom-right cell, return the distance
            if (row, col) == (max_row, max_col):
                return distance
            
            # Explore all valid neighbors
            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1  # Mark visited with distance
                queue.append((neighbor_row, neighbor_col))  # Add to BFS queue
        
        # If no path is found, return -1
        return -1

    
class Solution2:
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        # Helper function to find the neighbors of a given cell.
        def get_neighbours(row, col):
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                if not(0 <= new_row <= max_row and 0 <= new_col <= max_col):
                    continue
                if grid[new_row][new_col] != 0:
                    continue
                yield (new_row, new_col)
        
        # Check that the first and last cells are open. 
        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return -1
        
        # Set up the BFS.
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        current_distance = 1
        
        # Do the BFS.
        while queue:
            # Process all nodes at current_distance from the top-left cell.
            nodes_of_current_distance = len(queue)
            for _ in range(nodes_of_current_distance):
                row, col = queue.popleft()
                if (row, col) == (max_row, max_col):
                    return current_distance
                for neighbour in get_neighbours(row, col):
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    queue.append(neighbour)
            # We'll now be processing all nodes at current_distance + 1
            current_distance += 1
                    
        # There was no path.
        return -1 