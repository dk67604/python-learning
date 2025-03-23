'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., removing the head)
        dummy = ListNode(-1)
        dummy.next = head

        # Initialize two pointers: leader will go ahead n steps
        trailer = leader = dummy

        # Move leader n steps ahead
        for _ in range(n):
            leader = leader.next
            # If n is longer than the list, return original head
            if not leader:
                return head

        # Move both pointers until leader reaches the end
        # After this, trailer will be right before the node to be removed
        while leader.next:
            leader = leader.next
            trailer = trailer.next

        # Skip the nth node from the end
        trailer.next = trailer.next.next

        # Return the head of the modified list
        return dummy.next
