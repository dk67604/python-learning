class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def helper(node:TreeNode) -> int:
        nonlocal max_sum
        if not node:
            return 0
        
        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        max_sum = max(max_sum, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)

    helper(root)
    return max_sum