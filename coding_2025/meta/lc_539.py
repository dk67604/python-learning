'''
539. Minimum Time Difference
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Helper function to convert HH:MM time format to total minutes
        def convertToMins(timeStr: str) -> int:
            hours, mins = map(int, timeStr.split(":"))  # Split "HH:MM" and convert to integers
            return hours * 60 + mins  # Convert to total minutes (hours * 60 + minutes)

        # Convert all time strings to minutes
        minutes = [convertToMins(tp) for tp in timePoints]
        
        # Sort the times in ascending order
        minutes.sort()

        # Initialize min_diff to a large number
        min_diff = float('inf')

        # Compare adjacent time differences to find the minimum difference
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Handle circular time difference (difference between last and first time)
        circular_diff = 1440 - minutes[-1] + minutes[0]  # 1440 minutes in a day
        min_diff = min(min_diff, circular_diff)

        # Return the minimum time difference
        return min_diff
