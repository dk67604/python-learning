'''
https://leetcode.com/problems/container-with-most-water/

Time Complexity: O(n), where n is the number of elements in the height list.

Explanation: The algorithm uses a two-pointer approach, starting from both ends of the list and moving inward. In each iteration, at least one pointer moves closer to the other, so there are at most n iterations. Each step does constant-time operations, leading to an overall linear time complexity.

Space Complexity: O(1) since the algorithm uses only a fixed amount of extra space regardless of the input size.
'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0  # Stores the maximum water found so far

        # Initialize two pointers at both ends of the array
        left, right = 0, len(height) - 1

        # Loop while the two pointers haven't crossed
        while left < right:
            # Calculate the height and width of the current container
            # Height is determined by the shorter of the two lines
            # Width is the distance between the two lines
            water = min(height[left], height[right]) * (right - left)

            # Update maximum water if this container holds more
            max_water = max(max_water, water)

            # Move the pointer pointing to the shorter line inward
            # This is a greedy step: we want to try and find a taller line
            # because increasing the shorter line might increase area
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                # If both heights are equal, moving either is fine
                # So we move both inward to explore new pairs
                left += 1
                right -= 1

        # Return the maximum area found
        return max_water
