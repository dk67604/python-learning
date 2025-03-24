'''
https://leetcode.com/problems/meeting-rooms-ii/description/

✅ Time Complexity: O(n log n)
Where:

n is the number of meeting intervals.

Explanation:
Sorting intervals by start time:

Takes O(n log n) time.

Processing each interval:

Each heapq.heappush and heapq.heappop operation takes O(log k), where k is the size of the heap (≤ n).

In total, across all n intervals, heap operations take O(n log n) in the worst case.

So, overall time complexity:
O(n log n)

✅ Space Complexity: O(n)
Explanation:

In the worst case (all meetings overlap), you store all n end times in the min-heap.

So heap size can grow up to n → O(n) space.
'''

import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Returns the minimum number of meeting rooms required to accommodate all meetings.

        :param intervals: List of meeting time intervals [start, end]
        :return: Minimum number of meeting rooms needed
        """

        # Edge case: No meetings, no rooms needed
        if not intervals:
            return 0

        # Step 1: Sort all intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize a min heap to track meeting end times (rooms in use)
        # The heap stores the end times of meetings currently using a room
        free_rooms = []

        # Step 3: Add the end time of the first meeting to the heap
        # This means one meeting is using one room
        heapq.heappush(free_rooms, intervals[0][1])

        # Step 4: Process the remaining meetings
        for i in intervals[1:]:
            # If the earliest ending meeting ends before the current meeting starts
            # it means one room got free, we can reuse it
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)  # Free up the room

            # Push the current meeting's end time into the heap
            # This occupies a room (either reused or a new one)
            heapq.heappush(free_rooms, i[1])

        # Step 5: The size of the heap tells us how many rooms are in use at the peak
        return len(free_rooms)
