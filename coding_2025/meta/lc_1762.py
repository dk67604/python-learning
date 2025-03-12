'''
1762. Buildings With an Ocean View
Solved
Medium
Topics
Companies
Hint
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109
'''
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Given a list `heights` where `heights[i]` represents the height of a building,
        return a list of indices of buildings that have a clear ocean view.
        
        A building has an ocean view if all buildings to its right have a smaller height.
        
        Approach:
        - Use a **monotonic decreasing stack** to maintain indices of buildings with ocean views.
        - Iterate through the buildings **from left to right**.
        - Pop buildings from the stack that are **shorter or equal** to the current building.
        - Append the current building index to the stack.
        - The remaining buildings in the stack have ocean views.

        Time Complexity: O(N) (Each building is pushed and popped at most once)
        Space Complexity: O(N) (Stack stores at most N elements in the worst case)
        """
        
        stack = []  # Stack to store indices of buildings with ocean views

        # Step 1: Iterate through the buildings from left to right
        for i in range(len(heights)):
            # Step 2: Remove buildings that are blocked by the current building
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()  # Remove shorter or equal height buildings

            # Step 3: Append the current building index to the stack
            stack.append(i)

        # Step 4: Return the indices of buildings that have a clear ocean view
        return stack

# Left and Right View
class Solution2:
    def findBuildingsWithViews(self, heights: List[int]) -> List[int]:
        """
        Given a list `heights` where `heights[i]` represents the height of a building,
        return a list of indices of buildings that have either:
        - A left-side view (no taller building before it).
        - A right-side view (no taller building after it).
        
        Approach:
        - Use two monotonic stacks (one for the left view, one for the right view).
        - Merge results into a set and return sorted indices.
        
        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        def get_view_indices(heights: List[int], left_to_right: bool) -> List[int]:
            """ Helper function to compute left or right view indices using a stack. """
            stack = []
            indices = []
            n = len(heights)
            iterable = range(n) if left_to_right else range(n - 1, -1, -1)

            for i in iterable:
                while stack and heights[stack[-1]] <= heights[i]:
                    stack.pop()
                stack.append(i)
                indices.append(i)

            return set(indices)

        # Get buildings visible from the left and right
        left_view = get_view_indices(heights, left_to_right=True)
        right_view = get_view_indices(heights, left_to_right=False)

        # Combine both views and return sorted indices
        return sorted(left_view | right_view)
