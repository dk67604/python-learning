'''
314. Binary Tree Vertical Order Traversal
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        treeData = defaultdict(list)
        q = deque([root])
        cols = deque([0])
        _min = 0
        _max = 0
        res = []
        while q:
            node = q.popleft()
            col = cols.popleft()
            treeData[col].append(node.val)
            if node.left:
                q.append(node.left)
                cols.append(col - 1)
                _min = min(_min, col - 1)
            if node.right:
                q.append(node.right)
                cols.append(col + 1)
                _max = max(_max, col + 1)
            
        for i in range(_min, _max+1): 
            res.append(treeData.get(i))
        return res