class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    lca_node = None
    def find_lca(node: TreeNode, p: TreeNode, q: TreeNode):
        nonlocal lca_node
        if not node:
            return False
        node_is_p_or_q = node == p or node == q
        left_containse_p_or_q = find_lca(node.left, p, q)
        right_contains_p_or_q = find_lca(node.right, p, q)

        if (node_is_p_or_q + left_containse_p_or_q + right_contains_p_or_q == 2):
            lca_node = node
        return (node_is_p_or_q or left_containse_p_or_q or right_contains_p_or_q)
    find_lca(root, p, q)
    return lca_node




