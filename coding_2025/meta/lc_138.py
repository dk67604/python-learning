"""
# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # HashMap (Dictionary) to keep track of visited nodes and avoid duplicates
        visitedHash = {}

        def helper(node: 'Optional[Node]') -> 'Optional[Node]':
            nonlocal visitedHash  # Use the shared dictionary to track copied nodes
            
            # Base case: If node is None, return None
            if not node:
                return None
            
            # If the node is already copied, return the copied node from the hash map
            if node in visitedHash:
                return visitedHash[node]
            
            # Create a new node with the same value, but without setting next or random yet
            newNode = Node(node.val, None, None)
            
            # Store this newly created node in the hash map before recursion
            visitedHash[node] = newNode

            # Recursively copy the next node and random node
            newNode.next = helper(node.next)
            newNode.random = helper(node.random)
            
            return newNode  # Return the copied node
        
        # Start the recursion with the head node
        newHead = helper(head)
        return newHead
