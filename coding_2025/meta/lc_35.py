'''
23. Merge k Sorted Lists
Solved
Hard
Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ListNode.__lt__ = lambda self, other: self.val < other.val
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        dummy = ListNode(-1)
        curr  = dummy
        while heap:
            smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)
        
        return dummy.next
        