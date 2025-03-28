'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
Time Complexity: O(n)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head  # If the list is empty, just return

        def helper(curr):
            """
            Recursively flattens the list starting from `curr`.
            Returns the last node of the flattened list.
            """
            last = curr  # To track the tail of the flattened portion

            while curr:
                tempNext = curr.next  # Save next pointer in case we overwrite it

                if curr.child:
                    # Save the child head
                    child_head = curr.child

                    # Recursively flatten the child list, returns the tail of the child chain
                    child_tail = helper(child_head)

                    # Splice the child list into the main list
                    curr.next = child_head       # Connect current node to child head
                    child_head.prev = curr       # Set child's prev to current
                    curr.child = None            # Nullify the child pointer (as required)

                    # If there was a next node after current, attach it to the end of child list
                    if tempNext:
                        child_tail.next = tempNext
                        tempNext.prev = child_tail

                    # Update last to the end of the child list
                    last = child_tail

                    # Move current to the saved next pointer to continue flattening
                    curr = tempNext
                else:
                    # No child, just move to next node
                    last = curr
                    curr = curr.next

            return last  # Return the tail of the fully flattened list

        helper(head)  # Start recursive flattening from head
        return head   # Return head of flattened list
