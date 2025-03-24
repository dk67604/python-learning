'''
56. Merge Intervals
Solved
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
Seen this question in a real interview before?
1/5

Time Complexity: O(n log n), where n is the number of intervals.

Explanation:

The list of intervals is sorted by start time, which takes O(n log n) time.

Then, we iterate through the sorted list once to merge intervals, which takes O(n) time.

Therefore, the total time complexity is dominated by the sorting step: O(n log n).

Space Complexity: O(n) in the worst case.

Explanation:

We use an additional list merged to store the merged intervals.

In the worst case (no overlaps), all intervals are added to the result, so the space used is O(n).

The sort operation may also take extra space depending on the sorting algorithm (but typically not counted as extra in-place space usage).
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by the starting value of each interval
        # This ensures that overlapping intervals are adjacent in the list
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize an empty list to store merged intervals
        merged = []
        
        # Step 3: Start with the first interval as the `prev` interval to compare
        prev = intervals[0]

        # Step 4: Iterate through the rest of the intervals
        for interval in intervals[1:]:
            # If the current interval overlaps with `prev`, merge them
            if interval[0] <= prev[1]:  
                # Update the end time of `prev` to include the new interval
                prev[1] = max(prev[1], interval[1])
            else:
                # If no overlap, add `prev` to merged list and move to next interval
                merged.append(prev)
                prev = interval

        # Step 5: Add the last merged interval to the list
        merged.append(prev)
        
        # Step 6: Return the merged intervals list
        return merged

        
        