'''
https://leetcode.com/problems/the-maze/description/

✅ Time Complexity: O(m × n)
Where:

m = number of rows in the maze

n = number of columns

Explanation:
Each cell in the maze can be added to the queue at most once.

For each cell, you simulate rolling the ball in 4 directions, but:

The rolling continues until hitting a wall or boundary, not checking every cell repeatedly.

So although rolling may scan several cells per direction, the visited matrix prevents revisiting them.

➡️ Hence, even though you're scanning along paths, each cell is processed once → total time: O(m × n)

✅ Space Complexity: O(m × n)
visited matrix: O(m × n)

queue can hold up to O(m × n) positions in the worst case
'''

from collections import deque
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]  # Tracks visited stopping positions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]   # Right, Down, Up, Left

        queue = deque([start])  # Start BFS with the initial position
        visited[start[0]][start[1]] = True  # Mark the start as visited

        while queue:
            r, c = queue.popleft()  # Current position

            # Check if destination is reached
            if [r, c] == destination:
                return True

            # Explore all 4 directions
            for dr, dc in directions:
                # 🔁 Start rolling from current position
                # We use new_r, new_c to simulate rolling the ball without modifying r, c
                new_r, new_c = r, c

                # Roll until hitting a wall or boundary
                while (
                    0 <= new_r + dr < rows and
                    0 <= new_c + dc < cols and
                    maze[new_r + dr][new_c + dc] == 0
                ):
                    new_r += dr
                    new_c += dc

                # If the stopping position hasn't been visited yet, add it to the queue
                if not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    queue.append([new_r, new_c])

        # If BFS completes and destination is never reached
        return False
