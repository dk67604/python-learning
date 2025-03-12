'''
543. Diameter of Binary Tree
Solved
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Same as coding_2025/trees/max_path_sum.py
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Given a Binary Search Tree (BST), calculate the sum of values of all nodes
        that fall within the range [low, high].
        """
        
        res = 0  # Variable to store the accumulated sum

        # Depth-First Search (DFS) helper function
        def dfs(node: TreeNode) -> None:
            nonlocal res  # Allow modification of outer `res` variable

            if not node:  # Base case: If the node is None, return
                return

            # If the node's value is within the given range, add it to the sum
            if low <= node.val <= high:
                res += node.val

            # If the node's value is greater than 'low', continue searching the left subtree
            if low < node.val:
                dfs(node.left)

            # If the node's value is less than 'high', continue searching the right subtree
            if node.val < high:
                dfs(node.right)

        # Start DFS traversal from the root
        dfs(root)

        # Return the total sum of values within the given range
        return res
