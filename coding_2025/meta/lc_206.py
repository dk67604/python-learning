'''
https://leetcode.com/problems/reverse-linked-list/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node to head and previous node to None
        curr_node, prev_node = head, None

        # Traverse the list and reverse the links one by one
        while curr_node:
            next_node = curr_node.next   # Store the next node
            curr_node.next = prev_node   # Reverse the current node's pointer
            prev_node = curr_node        # Move prev_node one step forward
            curr_node = next_node        # Move curr_node one step forward

        # At the end, prev_node will be the new head of the reversed list
        return prev_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, return head
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse the link: the next node should now point back to the current node
        head.next.next = head

        # Break the current node's next pointer to avoid cycles
        head.next = None

        # Return the new head of the reversed list
        return new_head
