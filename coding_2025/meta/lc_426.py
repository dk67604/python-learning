'''
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Converts a Binary Search Tree (BST) into a circular doubly linked list
        using an in-order traversal.

        The left pointer acts as `prev`, and the right pointer acts as `next`.

        Approach:
        - Use an iterative **in-order traversal** with a stack.
        - Maintain a **`prevNode`** pointer to link nodes.
        - Keep track of the **firstNode (head)** and **lastNode (tail)**.
        - At the end, connect `firstNode` and `lastNode` to make it circular.

        Time Complexity: O(N) (each node is visited once)
        Space Complexity: O(N) (stack stores nodes during traversal)
        """

        if not root:
            return None  # Edge case: empty tree

        stack = []  # Stack for in-order traversal
        prevNode = None  # Previous node in in-order sequence
        currentNode = root  # Start traversal from root
        firstNode = None  # Head of the doubly linked list
        lastNode = None  # Tail of the doubly linked list

        # Step 1: Perform in-order traversal using a stack
        while stack or currentNode:
            # Traverse left subtree first (in-order)
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            
            # Pop the node from the stack (visit the node)
            node = stack.pop()

            # Step 2: Link the previous node (`prevNode`) to the current node
            node.left = prevNode  # Link current node's left to previous node
            if prevNode:
                prevNode.right = node  # Link previous node's right to current node
            
            # Update `prevNode` for the next iteration
            prevNode = node

            # Step 3: Set the first node (head) of the doubly linked list
            if not firstNode:
                firstNode = node  # The first node in in-order traversal is the head

            # Track the last node (tail)
            lastNode = node  # Keep updating the last node

            # Move to the right subtree
            currentNode = node.right

        # Step 4: Make the linked list circular
        firstNode.left = lastNode  # Connect head to tail
        lastNode.right = firstNode  # Connect tail to head

        # Step 5: Return the head (first node) of the circular doubly linked list
        return firstNode


        