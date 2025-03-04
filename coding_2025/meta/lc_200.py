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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,-1],[0,1]]
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        def dfs(i,j,visited):
            visited.add((i,j))
            for dr, dc in directions:
                r = i + dr
                c = j + dc
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c,visited)
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and  (i, j) not in visited:
                    island +=1
                    dfs(i,j, visited)
        return island
        