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

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMins(timeStr: str) -> int:
            hours, mins = map(int, timeStr.split(":"))
            return hours * 60 + mins  # Convert HH:MM to total minutes

        minutes = [convertToMins(tp) for tp in timePoints]
        minutes.sort()
        min_diff = float(inf)
        for i in range (1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])
        circular_diff = 1440 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, circular_diff)
        return min_diff