'''
1650. Lowest Common Ancestor of a Binary Tree III
Solved
Medium
Topics
Companies
Hint
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
"""
Find the depth of each pointer
Move the deeper pointer up until it is at the same level as the other pointer
Move each pointer up level-by-level until they meet
"""
class Solution:
    def get_depth(self, p):
        """
        Helper function to calculate the depth of a given node `p` in a tree.
        The depth is the distance from the node to the root.
        
        Args:
            p (Node): The node whose depth is to be calculated.
        
        Returns:
            int: Depth of the node in the tree.
        """
        depth = 0
        while p:  # Traverse upwards until the root node is reached
            p = p.parent
            depth += 1  # Increment depth counter
        return depth

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Finds the lowest common ancestor (LCA) of two nodes in a tree where nodes 
        have parent pointers.
        
        The approach:
        - Compute the depth of both nodes.
        - Move the deeper node up until both nodes are at the same level.
        - Move both nodes up together until they meet, which is the LCA.

        Args:
            p (Node): First node.
            q (Node): Second node.

        Returns:
            Node: The lowest common ancestor of p and q.
        """
        # Step 1: Compute the depth of both nodes
        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)

        # Step 2: Move the deeper node up so both nodes are at the same depth
        # If `p` is deeper, move `p` up
        for _ in range(p_depth - q_depth):
            p = p.parent

        # If `q` is deeper, move `q` up
        for _ in range(q_depth - p_depth):
            q = q.parent

        # Step 3: Move both nodes up simultaneously until they meet
        while p != q:
            p = p.parent
            q = q.parent

        # Step 4: Return the first common ancestor
        return p

        

        

        