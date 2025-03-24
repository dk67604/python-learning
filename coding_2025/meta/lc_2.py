'''
https://leetcode.com/problems/add-two-numbers/description/
O(max(n, m)), where n is the number of nodes in the first linked list l1, and m is the number of nodes in the second linked list l2.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the result list
        dummyNode = ListNode(0)
        curr = dummyNode  # Pointer to build the new list
        carry = 0         # Initialize carry to 0

        # Loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry != 0:
            # Get the current values, defaulting to 0 if node is None
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # Compute the sum and carry
            currentSum = l1_val + l2_val + carry
            carry = currentSum // 10  # Update carry for next iteration

            # Create a new node with the digit (remainder after division by 10)
            newNode = ListNode(currentSum % 10)
            curr.next = newNode       # Append to the result list
            curr = newNode            # Move pointer forward

            # Move to next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of dummy (skipping dummy head)
        return dummyNode.next
