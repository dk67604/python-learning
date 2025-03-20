'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) using a Min Heap.
        """
        minHeap = []  # Min-Heap to store distances along with points
        
        # Step 1: Compute squared distance and store in minHeap
        for x, y in points:
            dist = x**2 + y**2  # Squared Euclidean distance to avoid floating point calculations
            minHeap.append([dist, x, y])  # Store distance along with point coordinates
        
        # Convert the list into a heap in O(N) time
        heapq.heapify(minHeap)

        res = []  # Stores k closest points
        
        # Step 2: Extract k closest points
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Extract the closest point (smallest distance)
            res.append([x, y])  # Store the point in the result list
            k -= 1  # Decrease the count
        
        return res  # Return the list of k closest points


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) using a Max Heap.
        This approach is efficient when k is much smaller than the total number of points.
        """
        maxHeap = []  # Max Heap (simulated using negative values)
        
        # Step 1: Process each point and maintain a max heap of size k
        for x, y in points:
            dist = -(x**2 + y**2)  # Compute negative squared Euclidean distance
            heapq.heappush(maxHeap, [dist, x, y])  # Push distance with point
            
            # If the heap size exceeds k, remove the farthest point (largest negative value)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)  # Remove the point with the smallest negative distance (farthest point)
        
        res = []  # Stores the k closest points
        
        # Step 2: Extract the k closest points from the heap
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)  # Pop elements from the heap
            res.append([x, y])  # Append the point to the result
        
        return res  # Return the final list of k closest points
