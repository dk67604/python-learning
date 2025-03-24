'''
https://leetcode.com/problems/random-pick-index/description/

✅ __init__(self, nums: List[int])
Time Complexity: O(n)
Where n is the length of the input list nums.

You iterate through the list once and populate a hashmap (self.map) with indices for each number.

Space Complexity: O(n)
In the worst case (all elements are unique), each number has its own list of indices → total space = O(n).

✅ pick(self, target: int)
Time Complexity: O(1)
Dictionary lookup (self.map[target]) is O(1).

random.choice(indexes) is also O(1).

Space Complexity: O(1)
Only uses a few local variables; no additional space that grows with input.
'''
import random
from collections import defaultdict
from typing import List

class Solution:
    
    # Constructor: Preprocess the input list to store indices of each number
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)  # Dictionary to store lists of indices for each number
        
        # Iterate through the list and store the indices of each number in the dictionary
        for i, num in enumerate(nums):
            self.map[num].append(i)  # Append index of `num` to its corresponding list

    # Function to pick a random index of the target number
    def pick(self, target: int) -> int:
        indexes = self.map[target]  # Retrieve the list of indices where `target` appears
        return random.choice(indexes)  # Randomly select one index from the list

# Example usage:
# nums = [1, 2, 3, 3, 3]
# obj = Solution(nums)
# print(obj.pick(3))  # Randomly returns an index of '3' (either 2, 3, or 4)
