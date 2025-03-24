from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def largest_overlap_of_interval(intervals: List[Interval]) -> int:
    """
    Finds the maximum number of overlapping intervals at any point in time.

    Approach:
    - Use a sweep line algorithm:
        - Treat each start as +1 (entering an interval),
        - Treat each end as -1 (leaving an interval),
        - Keep track of how many intervals are active at each time point.
    """

    points = []

    # Step 1: Convert intervals to (time, type) points
    for interval in intervals:
        points.append((interval.start, 'S'))  # 'S' for start
        points.append((interval.end, 'E'))    # 'E' for end

    # Step 2: Sort points:
    # - First by time
    # - Second: make sure 'S' comes before 'E' when times are equal to ensure correct overlap count
    points.sort(key=lambda x: (x[0], x[1]))

    active_intervals = 0      # Number of currently overlapping intervals
    max_overlaps = 0          # Track maximum number of overlaps found

    # Step 3: Sweep through all points
    for time, point_type in points:
        if point_type == 'S':
            active_intervals += 1  # A new interval starts
        else:
            active_intervals -= 1  # An interval ends

        max_overlaps = max(max_overlaps, active_intervals)  # Update max

    return max_overlaps
