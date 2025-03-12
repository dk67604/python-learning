'''
Koko Eating Bananas
Solved
Medium
Topics
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
'''

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Given an array `piles` representing the number of bananas in each pile and
        `h` representing the number of hours available, find the minimum eating speed
        (bananas per hour) such that all bananas can be eaten within `h` hours.
        
        The problem is solved using **Binary Search** to find the optimal speed.
        """
        
        # Set the search space between 1 (slowest) and max(piles) (fastest)
        left, right = 1, max(piles)

        # Apply binary search to find the minimum feasible eating speed
        while left < right:
            mid = (left + right) // 2  # Middle speed
            if self.is_feasible(piles, mid, h):  
                # If it is possible to eat all bananas within h hours, try a slower speed
                right = mid
            else:
                # If not feasible, increase the speed
                left = mid + 1
        
        return left  # The minimum feasible eating speed
    

    def is_feasible(self, piles: List[int], mid: int, h: int) -> bool:
        """
        Helper function to check if a given speed `mid` allows us to eat all
        the bananas within `h` hours.
        """
        total_hours = 0  # Total hours required at this speed

        # Calculate the number of hours needed for each pile
        for pile in piles:
            # Using math.ceil(pile/mid) but rewritten to avoid import
            hour = (pile + mid - 1) // mid  # This is equivalent to ceil(pile/mid)
            total_hours += hour  # Accumulate total hours needed
        
        # Return True if the total hours required is within the allowed time h
        return total_hours <= h

