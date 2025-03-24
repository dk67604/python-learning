'''
https://leetcode.com/problems/closest-binary-search-tree-value/description/

✅ Solution 1: Inorder Traversal + Linear Search
Time Complexity: O(n)
Inorder traversal visits every node once → O(n)

Finding the closest value in the list using min(..., key=...) → O(n)

Total: O(n)

Space Complexity: O(n)
You store all node values in the values list → O(n)

Recursion stack (in worst case for unbalanced tree) → up to O(n)

✅ Solution 2: Optimized BST Traversal (Iterative)
Time Complexity: O(h), where h is the height of the BST
Each step of the traversal compares and moves either left or right, like binary search.

In a balanced BST, h = log n, so time is O(log n).

In a skewed BST, h = n, so time is O(n) in worst case.

Space Complexity: O(1)
No recursion or extra space used except a few variables.
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

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val  # Initialize closest with the root value
        
        while root:
            # Check if the current node is a better candidate for "closest"
            if (
                # ✅ Case 1: current node is strictly closer to target than previous closest
                abs(root.val - target) < abs(closest - target)
                
                # ✅ Case 2: current node is equally close but numerically smaller
                or (
                    abs(root.val - target) == abs(closest - target)  # Same distance
                    and root.val < closest                           # Prefer smaller value
                )
            ):
                # ✅ Update closest to current node's value
                closest = root.val
            
            # Move left if target is smaller, right if target is larger
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest

        


