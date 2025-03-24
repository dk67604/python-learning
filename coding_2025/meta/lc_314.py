'''
314. Binary Tree Vertical Order Traversal
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]

📌 Final Time Complexity:
🟩 O(n) — where n is the number of nodes in the binary tree

All operations are linear in the number of nodes. There are no nested loops or redundant traversals.

🧠 Space Complexity (Bonus):
treeData: stores each node once → O(n)

q and cols: hold up to one level of nodes at a time → O(w) where w = max width of the tree (worst case: O(n))

res: stores all node values grouped → O(n)

➡️ Overall space complexity: O(n)
'''

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: If the tree is empty, return an empty list
        if not root:
            return []
        
        # Dictionary to store node values grouped by their column index
        treeData = defaultdict(list)

        # Queue to perform level-order traversal (BFS)
        q = deque([root])

        # Queue to track the column index corresponding to each node
        cols = deque([0])  # Root starts at column index 0

        # Variables to track the minimum and maximum column indices
        _min = 0
        _max = 0

        # Result list to store the vertical order traversal
        res = []

        # Perform BFS traversal
        while q:
            # Pop the node and its corresponding column index
            node = q.popleft()
            col = cols.popleft()

            # Store the node's value in the corresponding column index
            treeData[col].append(node.val)

            # If the node has a left child, add it to the queue with col - 1
            if node.left:
                q.append(node.left)
                cols.append(col - 1)
                _min = min(_min, col - 1)  # Update the minimum column index

            # If the node has a right child, add it to the queue with col + 1
            if node.right:
                q.append(node.right)
                cols.append(col + 1)
                _max = max(_max, col + 1)  # Update the maximum column index
            
        # Collect results in order of column indices from _min to _max
        for i in range(_min, _max + 1): 
            res.append(treeData.get(i))

        return res
