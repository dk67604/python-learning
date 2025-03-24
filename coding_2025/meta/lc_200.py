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

🧠 Time and Space Complexity:
Time Complexity: O(m × n) — Each cell is visited once.

Space Complexity: O(m × n) — In the worst case, the visited set and recursion stack can grow to cover all land cells.
'''

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define possible movement directions (down, up, left, right)
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Variable to count the number of islands
        island = 0
        
        # Depth-First Search (DFS) function to explore an island
        def dfs(i, j, visited):
            visited.add((i, j))  # Mark current cell as visited

            # Explore all 4 directions
            for dr, dc in directions:
                r, c = i + dr, j + dc
                if (
                    0 <= r < rows and
                    0 <= c < cols and
                    grid[r][c] == '1' and
                    (r, c) not in visited
                ):
                    dfs(r, c, visited)  # Recurse on connected land

        visited = set()  # Set to track visited cells

        # Iterate through all grid cells
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island += 1           # Found a new island
                    dfs(i, j, visited)    # Explore the entire island

        return island  # Return total number of islands

         

        