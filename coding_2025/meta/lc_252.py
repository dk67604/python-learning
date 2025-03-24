'''
https://leetcode.com/problems/meeting-rooms/
'''

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Determines if a person can attend all meetings without any time overlap.

        :param intervals: List of meeting time intervals [start, end]
        :return: True if no meetings overlap, False otherwise
        """

        # Edge case: no meetings at all
        if not intervals:
            return True

        # Step 1: Sort all intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize previous meeting to the first one
        prev = intervals[0]

        # Step 3: Iterate through the rest of the meetings
        for interval in intervals[1:]:
            # If the current meeting starts before the previous one ends, they overlap
            if interval[0] < prev[1]:
                return False  # Can't attend both meetings

            # Otherwise, update the previous meeting to current
            prev = interval

        # Step 4: If we never found an overlap, return True
        return True
