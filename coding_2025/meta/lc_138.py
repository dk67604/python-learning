'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/

Time Complexity: O(n), where n is the number of nodes in the linked list.

Explanation:

Each node in the original list is visited exactly once.

For each node, you:

Create a copy,

Recursively visit its .next and .random pointers.

The visitedHash dictionary ensures no node is visited or copied more than once.

Therefore, the total work is proportional to the number of nodes: O(n).

Space Complexity: O(n)

Explanation:

A hash map (visitedHash) is used to store a mapping from original nodes to their copies. It stores one entry per node → O(n) space.

Additionally, recursive calls consume stack space. In the worst case (if the list is a single chain), the recursion stack could go up to n levels → O(n) space.

So, the overall space complexity is O(n).

'''

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random


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
