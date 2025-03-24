'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
'''

from typing import List
from math import inf

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Returns the minimum number of intervals to remove to make the rest non-overlapping.

        Approach:
        - Use a greedy algorithm by always keeping the interval with the earliest end time.
        - Sort intervals by end time to maximize how many non-overlapping intervals can be kept.
        """

        # Step 1: Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])

        ans = 0         # Count of intervals to remove
        k = -inf        # End of the last non-overlapping interval

        # Step 2: Iterate through each interval
        for x, y in intervals:
            if x >= k:
                # Case 1: No overlap — we can keep this interval
                k = y  # Update the end of last kept interval
            else:
                # Case 2: Overlap — we must remove this interval
                ans += 1

        return ans
