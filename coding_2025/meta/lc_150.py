'''
https://leetcode.com/problems/merge-intervals/description/

✅ Time Complexity: O(n log n), where n is the number of intervals.
Explanation:

Sorting the list of intervals by their start time takes O(n log n).

Iterating through the sorted intervals and merging them takes O(n) time.

So the total time complexity is dominated by the sorting step: O(n log n).

✅ Space Complexity: O(n)
Explanation:

In the worst case (no overlapping intervals), all intervals are added to the merged list → O(n) space.

Although the sorting may be done in-place depending on the implementation, the output list still requires space.

🧠 Summary:
Time Complexity: O(n log n)

Space Complexity: O(n)
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
