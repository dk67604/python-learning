# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        current = root

        while stack or current:
            # Step 1: Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Step 2: Process the node
            current = stack.pop()
            result.append(current.val)

            # Step 3: Visit the right subtree
            current = current.right

        return result
