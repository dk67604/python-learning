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

Time Complexity: O(N log k), where:

k is the number of linked lists,

N is the total number of nodes across all lists.

Explanation:

Each node is inserted into and removed from the min-heap exactly once.

Inserting or removing from a heap of size k takes O(log k) time.

Since there are N nodes in total, the overall time complexity is O(N log k).

Space Complexity: O(k)

Explanation:

The min-heap holds at most k nodes at any time (one from each list).

Aside from the heap and the output list (which doesn't count as extra space), no additional data structures are used.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min heap to store the smallest elements from k linked lists
        heap = []
        
        # Define a custom comparator for ListNode objects to allow heapq to work
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        # Push the head node of each linked list into the heap
        for head in lists:
            if head:  # Only push non-empty lists
                heapq.heappush(heap, head)

        # Dummy node to serve as the starting point of the merged linked list
        dummy = ListNode(-1)
        curr = dummy  # Pointer to track the current position in the merged list

        # Process the heap until all nodes are merged
        while heap:
            # Extract the smallest node from the heap
            smallest_node = heapq.heappop(heap)
            # Append it to the merged list
            curr.next = smallest_node
            curr = curr.next  # Move the pointer forward
            
            # If there are more nodes in the current list, push the next node into the heap
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)

        # Return the merged linked list (excluding the dummy node)
        return dummy.next

        