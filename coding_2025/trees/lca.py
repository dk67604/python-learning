class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the Lowest Common Ancestor (LCA) of two nodes in a binary tree.

    The LCA is defined as the lowest node in the tree that has both `p` and `q` as descendants 
    (where we allow a node to be a descendant of itself).

    :param root: The root of the binary tree
    :param p: First node
    :param q: Second node
    :return: The lowest common ancestor node of `p` and `q`
    """

    lca_node = None  # Variable to store the Lowest Common Ancestor

    def find_lca(node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        """
        Recursively searches for `p` and `q` in the binary tree and identifies the LCA.

        :param node: Current node being processed
        :param p: First node
        :param q: Second node
        :return: Boolean indicating whether `p` or `q` is found in the subtree rooted at `node`
        """
        nonlocal lca_node  # Allows modifying `lca_node` from the inner function
        
        if not node:  
            return False  # Base case: If the node is None, return False

        # Check if the current node is either `p` or `q`
        node_is_p_or_q = node == p or node == q
        
        # Recursively search in the left subtree
        left_contains_p_or_q = find_lca(node.left, p, q)
        
        # Recursively search in the right subtree
        right_contains_p_or_q = find_lca(node.right, p, q)

        # If any two of the three conditions (current node is `p` or `q`, left subtree contains `p` or `q`,
        # right subtree contains `p` or `q`) are true, then the current node is the LCA
        if (node_is_p_or_q + left_contains_p_or_q + right_contains_p_or_q) >= 2:
            lca_node = node  # Update the LCA node

        # Return True if `p` or `q` is found in this node or any of its subtrees
        return node_is_p_or_q or left_contains_p_or_q or right_contains_p_or_q

    # Start the recursive search from the root
    find_lca(root, p, q)

    # Return the LCA node
    return lca_node
