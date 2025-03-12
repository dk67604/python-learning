'''
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define possible movement directions (right, left, up, down)
        directions = [[1,0], [-1,0], [0,-1],[0,1]]
        
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Variable to count the number of islands
        island = 0
        
        # Depth-First Search (DFS) function to explore an island
        def dfs(i, j, visited):
            # Mark the current cell as visited
            visited.add((i, j))
            
            # Explore all four possible directions (up, down, left, right)
            for dr, dc in directions:
                r = i + dr  # New row index
                c = j + dc  # New column index
                
                # Check if the new position is within bounds, is land ('1'), and not visited
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c, visited)  # Recursively visit adjacent land cells
        
        # Set to keep track of visited cells
        visited = set()
        
        # Iterate through the grid to find unvisited land cells ('1')
        for i in range(rows):
            for j in range(cols):
                # If the cell is land and hasn't been visited, it's a new island
                if grid[i][j] == '1' and (i, j) not in visited:
                    island += 1  # Increment the island count
         

        