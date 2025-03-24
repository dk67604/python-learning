'''
https://leetcode.com/problems/nested-list-weight-sum/description/
339. Nested List Weight Sum
Solved
Medium
Topics
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0

✅ Time Complexity: O(n)
Where:

n is the total number of elements in the entire nested structure, including both integers and lists.

Why?
You visit every element exactly once, whether it's:

an integer → multiply it by its depth

or a list → recursively traverse it

So the number of isInteger(), getInteger(), and getList() calls is proportional to the number of total elements → O(n)

✅ Space Complexity:
DFS version: O(d) — where d is the maximum depth of nesting

Comes from the recursion stack

BFS version: O(w) — where w is the maximum number of elements at any level

Comes from the queue
'''
from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def __init__(self, value=None):
#         """
#         If value is not specified, initializes an empty list.
#         Otherwise initializes a single integer equal to value.
#         """
#
#     def isInteger(self):
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         :rtype bool
#         """
#
#     def add(self, elem):
#         """
#         Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#         :rtype void
#         """
#
#     def setInteger(self, value):
#         """
#         Set this NestedInteger to hold a single integer equal to value.
#         :rtype void
#         """
#
#     def getInteger(self):
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         :rtype int
#         """
#
#     def getList(self):
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         :rtype List[NestedInteger]
#         """

class Solution:
    def depthSum(self, nestedList: List["NestedInteger"]) -> int:
        # Helper function to perform DFS (Depth-First Search)
        def helper(nested, depth):
            total = 0  # Local sum at this depth level
            
            # Iterate through each element in the nested list
            for item in nested:
                if item.isInteger():
                    # If it's an integer, multiply it by the depth and add to total
                    total += depth * item.getInteger()
                else:
                    # If it's a list, recursively call helper function with increased depth
                    total += helper(item.getList(), depth + 1)
            
            return total  # Return the accumulated sum at this level
        
        # Start the recursive function with depth 1
        return helper(nestedList, 1)

from typing import List
from collections import deque

'''
Time: O(n), where n is the total number of NestedInteger elements (including those nested)

Space: O(n) for the queue in the worst case


'''
class Solution2:
    def depthSum(self, nestedList: List['NestedInteger']) -> int:
        total = 0
        queue = deque([(item, 1) for item in nestedList])  # Each element is (NestedInteger, depth)

        while queue:
            current, depth = queue.popleft()

            if current.isInteger():
                total += current.getInteger() * depth
            else:
                for ni in current.getList():
                    queue.append((ni, depth + 1))  # Increase depth for nested list

        return total
