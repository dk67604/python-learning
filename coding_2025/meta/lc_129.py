'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n), where n is the number of nodes in the binary tree.
Explanation:

Each node is visited exactly once during the depth-first traversal.

At each node, constant-time operations are performed (multiplication, addition, pushing to stack).

Therefore, the total time is proportional to the number of nodes: O(n)

✅ Space Complexity: O(h), where h is the height of the tree.
Explanation:

The space used by the stack depends on the depth of the recursion (or stack) at any time.

In the worst case:

For a skewed tree (like a linked list), the height is n, so space = O(n)

For a balanced tree, height = log n, so space = O(log n)

Therefore, space complexity is O(h), where h is the height of the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Computes the sum of all root-to-leaf numbers in a binary tree.
        
        Each root-to-leaf path represents a number formed by concatenating node values.
        The sum of all such numbers is returned.

        :param root: Root node of the binary tree
        :return: Sum of all root-to-leaf numbers
        """
        
        # Stack for iterative depth-first traversal (node, current number)
        stack = [(root, 0)]
        
        # Variable to store the sum of all root-to-leaf numbers
        root_to_leaf = 0 
        
        # Iterate using DFS (Depth-First Search)
        while stack:
            root, curr_number = stack.pop()  # Get the current node and its accumulated value
            
            if root is not None:
                # Update the current number by shifting left (multiplying by 10) and adding node value
                curr_number = curr_number * 10 + root.val

                # If it's a leaf node, add the current number to the total sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    # Push the right child first (so left is processed first in DFS order)
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf  # Return the sum of all root-to-leaf numbers