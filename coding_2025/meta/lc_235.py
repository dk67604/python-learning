'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(h), where h is the height of the BST.
Explanation:

You traverse the tree starting from the root, going either left or right depending on the values of p and q.

In the best case (balanced BST), height h = log n, so time is O(log n).

In the worst case (unbalanced BST or skewed tree), height h = n, so time is O(n).

✅ Space Complexity:
Iterative version (your code): O(1)

You use no recursion and only a few variables — constant space.
Recursive version (if you used recursion): O(h) for the recursion stack.

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the Lowest Common Ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        The LCA of `p` and `q` in a BST is defined as the lowest node in the tree
        that has both `p` and `q` as descendants.

        Since it's a BST:
        - If both `p` and `q` are smaller than `root`, the LCA must be in the left subtree.
        - If both `p` and `q` are greater than `root`, the LCA must be in the right subtree.
        - If `p` and `q` are on different sides, `root` is the LCA.

        :param root: The root of the BST.
        :param p: First node in the BST.
        :param q: Second node in the BST.
        :return: The lowest common ancestor node of `p` and `q`.
        """
        
        while root:
            # If both `p` and `q` are smaller than `root`, move to the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left  

            # If both `p` and `q` are greater than `root`, move to the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  

            # If `p` and `q` are on different sides, or one of them is `root`, we found the LCA
            else:
                return root  # This is the lowest common ancestor

        return None  # If no LCA is found (shouldn't happen in a valid BST)
