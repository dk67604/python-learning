'''
https://leetcode.com/problems/moving-average-from-data-stream/
'''

class MovingAverage:

    def __init__(self, size: int):
        self.nums = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.nums.append(val)
        if len(self.nums) <= self.size:
            return sum(self.nums)/len(self.nums)
        else:
            start = len(self.nums) - self.size
            return sum(self.nums[start:len(self.nums)]) / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage2:

    def __init__(self, size: int):
        self.sum = 0
        self.size = size
        self.window = deque()
        

    def next(self, val: int) -> float:
        self.sum +=val
        self.window.append(val)
        if len(self.window) > self.size:
            self.sum -= self.window.popleft()
        
        return self.sum/len(self.window)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)