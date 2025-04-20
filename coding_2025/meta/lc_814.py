'''
https://leetcode.com/problems/binary-tree-pruning/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node: TreeNode) -> bool:
            if not node:
                return False
            
            # Check if any node in the left subtree contains a 1.
            left_contains_one = helper(node.left)
            
            # Check if any node in the right subtree contains a 1.
            right_contains_one = helper(node.right)

              # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one: 
                node.left = None
                
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one: 
                node.right = None
            
            return node.val or left_contains_one or right_contains_one

        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if helper(root) else None
        