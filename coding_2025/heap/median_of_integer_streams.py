import heapq
class MedianFinder:

    def __init__(self):
        self.left_half = [] #Max Heap
        self.right_half = [] # Min heap
        

    def addNum(self, num: int) -> None:
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)

            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        
        else:
            heapq.heappush(self.right_half, num)
            if len(self.left_half) < len(self.right_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))
        

    def findMedian(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0

        return -self.left_half[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()