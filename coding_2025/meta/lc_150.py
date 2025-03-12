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
