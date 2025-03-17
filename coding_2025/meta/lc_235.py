'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
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
