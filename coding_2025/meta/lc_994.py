'''
https://leetcode.com/problems/rotting-oranges/

✅ Time Complexity: O(m × n)
Where:

m is the number of rows in the grid.

n is the number of columns.

🔍 Why?
Grid Traversal (Initialization)

You traverse the entire grid once to:

Count fresh oranges.

Add all rotten oranges to the queue.

This takes O(m × n).

BFS Traversal

In the worst case, every cell with a fresh orange gets visited exactly once and turned rotten.

So again, BFS will process each cell at most once → O(m × n).

Hence, the overall time complexity is:

✅ O(m × n)

✅ Space Complexity: O(m × n)
In the worst case, the queue can hold all the rotten oranges → up to O(m × n).

You also use a few variables like ones, seconds, and a directions list of constant size, which is negligible.

So:

✅ Space Complexity = O(m × n)

'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Directions for moving up, down, left, and right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()  # Queue for BFS traversal
        ones = 0  # Count of fresh oranges (1s)
        seconds = 0  # Timer to count minutes

        # Helper function to check if a cell is within grid bounds
        def is_within_bounds(r: int, c: int):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        # Step 1: Count fresh oranges and enqueue all rotten ones
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:  # Fresh orange found
                    ones += 1
                elif grid[r][c] == 2:  # Rotten orange found
                    queue.append((r, c))  # Add to BFS queue

        # Step 2: Perform BFS to spread rot
        while queue and ones > 0:  # Continue while there are fresh oranges
            seconds += 1  # Increase time as each minute passes

            # Process all currently rotten oranges in queue
            for _ in range(len(queue)):
                r, c = queue.popleft()  # Get the next rotten orange
                
                # Try all 4 possible directions (up, down, left, right)
                for d in dirs:
                    next_r, next_c = r + d[0], c + d[1]

                    # Check if the next cell is within bounds and has a fresh orange
                    if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 2  # Make it rotten
                        queue.append((next_r, next_c))  # Add to queue for next round
                        ones -= 1  # Reduce count of fresh oranges

        # Step 3: If no fresh oranges are left, return elapsed time; otherwise, return -1
        return seconds if ones == 0 else -1

        