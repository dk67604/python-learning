'''
https://leetcode.com/problems/add-two-numbers-ii/description/

✅ Time Complexity: O(m + n)
Where:

m = length of linked list l1

n = length of linked list l2

Breakdown:
Reversing both lists:

reverse_list(l1) takes O(m)

reverse_list(l2) takes O(n)

Adding corresponding digits:

You iterate through both reversed lists once → up to O(max(m, n))

Total time:

scss
Copy
Edit
O(m + n) for reversal + O(max(m, n)) for addition
⇒ O(m + n)
✅ Space Complexity: O(m + n)
In the worst case, the sum may have one more digit than either input (e.g., 999 + 1 = 1000)

So, you create a new linked list of up to max(m, n) + 1 nodes → O(m + n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Helper function to reverse a linked list
        def reverse_list(node: Optional[ListNode]) -> Optional[ListNode]:
            curr, prev = node, None
            while curr:
                next_node = curr.next  # Store next node
                curr.next = prev       # Reverse the pointer
                prev = curr            # Move prev to current
                curr = next_node       # Move to next node
            return prev  # New head of reversed list

        # Reverse both input lists to make addition easier from least significant digit
        r1 = reverse_list(l1)
        r2 = reverse_list(l2)

        carry = 0
        ans = None  # Initialize result list as empty

        # Loop until all nodes and carry are processed
        while r1 or r2 or carry:
            total_sum = carry  # Start with carry from previous addition

            # Add digit from first list if available
            if r1:
                total_sum += r1.val
                r1 = r1.next

            # Add digit from second list if available
            if r2:
                total_sum += r2.val
                r2 = r2.next

            # Update carry for next step
            carry = total_sum // 10

            # Create new node with current digit (mod 10)
            new_node = ListNode(total_sum % 10)

            # Prepend the new node to the result list
            new_node.next = ans
            ans = new_node

        # Return the head of the result list
        return ans 
