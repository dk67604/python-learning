'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
Time Complexity: O(n)
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None  # Return if the list is empty

        # Create a dummy node to simplify edge cases
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = [head]  # Use a stack for depth-first traversal

        while stack:
            curr = stack.pop()  # Pop the current node to process

            # Connect current node with the previous node
            prev.next = curr
            curr.prev = prev

            # If there is a next node, push it onto the stack.
            # It will be processed after the child node (if any)
            if curr.next:
                stack.append(curr.next)

            # If there is a child node, push it to the stack to be processed next
            # Set curr.child to None as it's flattened now
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # Important to remove child reference

            # Move prev forward for the next iteration
            prev = curr

        # Detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next  # Return the flattened list starting from the real head

