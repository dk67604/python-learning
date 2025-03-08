class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_search_tree_validations(root: TreeNode) -> bool:
    return is_within_bounds(root, float('-inf'), float('+inf'))


def is_within_bounds(node: TreeNode, lower_bound: int, upper_bound: int):
    if not node:
        return True

    if not lower_bound < node.val < upper_bound:
        return False

    if not is_within_bounds(node.left, lower_bound, node.val):
        return False
    
    return is_within_bounds(node.right, node.val, upper_bound)
