'''
https://leetcode.com/problems/closest-binary-search-tree-value/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = []  # List to store the inorder traversal values

        def inorder(node: Optional[TreeNode]):
            """Recursive function to perform inorder traversal (Left -> Root -> Right)."""
            nonlocal values  # Use nonlocal to modify the values list
            if node:
                inorder(node.left)   # Visit the left subtree
                values.append(node.val)  # Process the current node
                inorder(node.right)  # Visit the right subtree

        inorder(root)  # Start the inorder traversal
        
        # Find the value in the list that is closest to the target
        return min(values, key=lambda x: abs(target - x))  

    def closestValue2(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) < (closest - target):
                closest = root.val
            root = root.left if target < root.left else root.right
        return closest

