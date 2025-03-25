'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Time Complexity: O(n * log W)

n is the number of packages (len(weights)).

W is the sum of all weights (sum(weights)), which defines the upper bound of the binary search range.

The algorithm performs a binary search over possible capacities in the range [max(weights), sum(weights)], which takes log W steps.

For each binary search step, the canShip() function runs in O(n) time to simulate the shipping process.

So, the total time complexity is O(n * log W).

Space Complexity: O(1)

The solution uses only a constant amount of extra space (for variables like left, right, mid, current_load, etc.).

No additional data structures are used that grow with input size.



'''

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Finds the minimum ship capacity to ship all packages within the given number of days.
        Uses binary search between the heaviest single package and the total weight.
        """

        # The minimum possible capacity must be at least the heaviest package
        left = max(weights)

        # The maximum possible capacity is the total weight (if we ship everything in one day)
        right = sum(weights)

        # Perform binary search to find the minimum feasible capacity
        while left < right:
            mid = (left + right) // 2  # Candidate capacity to test
            if self.canShip(weights, mid, days):
                right = mid  # Try a smaller capacity
            else:
                left = mid + 1  # Need a larger capacity

        # When left == right, we've found the smallest feasible capacity
        return left

    def canShip(self, weights: List[int], capacity: int, days: int) -> bool:
        """
        Helper function to check if all weights can be shipped within `days`
        using the given `capacity`.
        """
        days_needed = 1
        current_load = 0

        for weight in weights:
            current_load += weight

            # If current load exceeds capacity, we need an extra day
            if current_load > capacity:
                days_needed += 1       # Increment day count
                current_load = weight  # Start new day with current package

        # Return True if we can do it within the allowed number of days
        return days_needed <= days
