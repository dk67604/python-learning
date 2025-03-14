'''
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        # Case 1: If the list is empty, create a new node that points to itself (circular list)
        if head is None:
            newNode = Node(insertVal)
            newNode.next = newNode  # Point to itself to maintain circular structure
            return newNode
        
        prev, curr = head, head.next  # Initialize two pointers
        insertFlag = False  # Flag to indicate whether insertion position is found

        while True:
            # Case 2: Insert between two nodes in a sorted manner (normal case)
            if prev.val <= insertVal <= curr.val:
                insertFlag = True

            # Case 3: Handling the wrap-around case (largest to smallest in circular list)
            elif prev.val > curr.val:
                # Insert if the value is either the new maximum or the new minimum in the list
                if insertVal >= prev.val or insertVal <= curr.val:
                    insertFlag = True
            
            # Insert the new node if a valid position is found
            if insertFlag:
                prev.next = Node(insertVal, curr)
                return head

            # Move to the next pair of nodes
            prev, curr = curr, curr.next

            # Case 4: If we have traversed the entire list and found no valid position
            if prev == head:
                break
        
        # Case 5: If all values in the list are the same or no valid position was found, insert anywhere
        prev.next = Node(insertVal, curr)
        return head
