import heapq

class MedianFinder:
    def __init__(self):
        # Max Heap (simulated using negatives) for the smaller half of the numbers
        self.left_half = []   # Ex: [-5, -3, -2] means actual values are [5, 3, 2]

        # Min Heap for the larger half of the numbers
        self.right_half = []  # Ex: [6, 8, 9] means actual values are [6, 8, 9]

    def addNum(self, num: int) -> None:
        """
        Adds a number into the data structure while maintaining balance between two heaps.
        """

        # Step 1: Add number to max heap (left_half) if empty or smaller than max of left_half
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)  # Push as negative to simulate max heap

            # If left_half has more than 1 extra element than right_half, rebalance
            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))

        # Step 2: Otherwise, add to min heap (right_half)
        else:
            heapq.heappush(self.right_half, num)

            # If right_half ends up bigger than left_half, rebalance
            if len(self.left_half) < len(self.right_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def findMedian(self) -> float:
        """
        Returns the median of all numbers added so far.
        """

        # Case 1: Even number of elements → median is the average of two middle elements
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0

        # Case 2: Odd number of elements → median is the middle from left_half
        return -self.left_half[0]
