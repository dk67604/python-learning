class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_binary_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    inorder_index_map = {}
    preorder_index = 0
    for i , val in enumerate(inorder):
        inorder_index_map[val] = i
    def helper(left:int, right: int) -> Optional[TreeNode]:
        # No element in range return None
        nonlocal preorder_index
        if left > right:
            return None
        val = preorder[preorder_index]
        node = TreeNode(val)
        preorder_index +=1
        inorder_index = inorder_index_map[val]
        node.left = helper(left, inorder_index - 1  )
        node.right = helper(inorder_index + 1, right)
        return node

    return helper(0, len(inorder) -1)    


