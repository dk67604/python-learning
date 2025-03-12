from typing import List
from collections import deque

# Multi-Source BFS Approach to Compute the Minimum Time for Infection Spread
def matrix_infection(grid: List[List[int]]) -> int:
    """
    Given a grid where:
    - `0` represents an empty cell.
    - `1` represents a healthy (uninfected) cell.
    - `2` represents an infected cell.

    The function determines the minimum time required for all healthy (`1`) cells 
    to become infected. If it's impossible to infect all cells, return `-1`.

    Approach:
    - Use Multi-Source BFS to spread the infection from all initial infected (`2`) cells.
    - Track the number of remaining healthy (`1`) cells.
    - If, after BFS traversal, there are still healthy cells, return `-1`.

    Time Complexity: O(M * N), where M and N are the grid dimensions.
    Space Complexity: O(M * N) for BFS queue in the worst case.
    """

    # Directions for moving up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Queue for BFS and counter for uninfected (`1`) cells
    queue = deque()
    ones = 0  # Count of uninfected cells
    seconds = 0  # Timer to track infection spread duration

    # Helper function to check if a cell is within grid bounds
    def is_within_bounds(r: int, c: int):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    # Step 1: Populate the queue with initially infected (`2`) cells
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                ones += 1  # Count healthy cells
            elif grid[r][c] == 2:
                queue.append((r, c))  # Add infected cells to BFS queue

    # Step 2: Perform Multi-Source BFS to spread the infection
    while queue and ones > 0:
        seconds += 1  # Increase time step

        # Process all infected cells at the current time step
        for _ in range(len(queue)):
            r, c = queue.popleft()
            
            # Try infecting neighboring healthy cells
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]

                # Check if the neighboring cell is within bounds and is healthy
                if is_within_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                    grid[next_r][next_c] = 2  # Infect the cell
                    queue.append((next_r, next_c))  # Add newly infected cell to queue
                    ones -= 1  # Decrease count of uninfected cells

    # Step 3: Return the total time if all cells are infected, otherwise return -1
    return seconds if ones == 0 else -1


