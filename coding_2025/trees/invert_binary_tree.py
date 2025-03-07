class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invert_binary_tree_recusrive(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_binary_tree_recusrive(root.left)
    invert_binary_tree_recusrive(root.right)
    return root

def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
        if node and node.left:
            stack.append(node.left)
        if node and node.right:
            stack.append(node.right)
    return root