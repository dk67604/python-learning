'''
938. Range Sum of BST
Solved
Easy
Topics
Companies
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        Recursively calculates the sum of all nodes within the range [low, high].
        Uses BST properties to prune unnecessary branches.
        """
        if not root:
            return 0  # Base case: return 0 if node is None

        elif root.val < low:
            # If current node is less than the low value, search only in the right subtree
            return self.rangeSumBST(root.right, low, high)

        elif root.val > high:
            # If current node is greater than high value, search only in the left subtree
            return self.rangeSumBST(root.left, low, high)

        # If current node is within range, include its value and explore both subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# Using DFS
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Uses Depth-First Search (DFS) to calculate the sum of nodes within the range [low, high].
        """
        res = 0  # Stores the sum of nodes in the range

        # Helper function to perform DFS
        def dfs(node: TreeNode) -> None:
            nonlocal res  # Use the outer `res` variable
            if not node:
                return  # Base case: return if node is None

            # If node is within range, add its value to the sum
            if low <= node.val <= high:
                res += node.val

            # If node value is greater than low, explore the left subtree
            if low < node.val:
                dfs(node.left)

            # If node value is less than high, explore the right subtree
            if node.val < high:
                dfs(node.right)

        dfs(root)  # Start DFS traversal from the root
        return res
