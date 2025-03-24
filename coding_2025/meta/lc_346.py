'''
https://leetcode.com/problems/moving-average-from-data-stream/

⏱ Time Complexity:
append: O(1)

sum(self.nums[start:]): O(k) where k = size
(slicing and summing the window takes linear time per call)

💾 Space Complexity: O(n)
The list self.nums stores all values received, even outside the window.
'''

class MovingAverage:

    def __init__(self, size: int):
        self.nums = []       # List to store all incoming values
        self.size = size     # Size of the moving window

    def next(self, val: int) -> float:
        self.nums.append(val)  # Add the new value to the list

        if len(self.nums) <= self.size:
            # If total values seen so far are fewer than window size
            return sum(self.nums) / len(self.nums)
        else:
            # Use only the last `size` values from the list
            start = len(self.nums) - self.size
            return sum(self.nums[start:]) / self.size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

'''
⏱ Time Complexity:
append: O(1)

popleft: O(1)

sum is maintained incrementally → O(1) per next() call

💾 Space Complexity: O(k)
Only the most recent k = size values are stored in the queue.
'''

from collections import deque

class MovingAverage2:

    def __init__(self, size: int):
        self.sum = 0                    # Running sum of the current window
        self.size = size               # Maximum size of the window
        self.window = deque()          # Store only the last `size` elements

    def next(self, val: int) -> float:
        self.sum += val                # Add the new value to the sum
        self.window.append(val)        # Add to the sliding window

        if len(self.window) > self.size:
            # If window is full, remove the oldest value
            self.sum -= self.window.popleft()

        return self.sum / len(self.window)  # Return the average




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)