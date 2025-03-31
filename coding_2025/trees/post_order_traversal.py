# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []       # Stack to simulate the recursion
        result = []      # Stores the postorder traversal result
        prev = None      # Pointer to track the last visited node
        current = root   # Start traversal from the root node

        while stack or current:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left
            
            # Peek at the top node in the stack
            node = stack[-1]

            # Case 1: If the node has no right child, OR
            # Case 2: If we already visited its right child (coming back up)
            if not node.right or node.right == prev:
                result.append(node.val)  # Process the current node
                prev = node              # Mark this node as visited
                stack.pop()             # Remove it from the stack
                current = None          # Prevent reprocessing this node
            else:
                # Go right if it hasn't been visited yet
                current = node.right

        return result
