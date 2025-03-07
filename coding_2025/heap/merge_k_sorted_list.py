import heapq
from typing import List
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

def combine_sorted_linked_list(lists: List[ListNode]) -> ListNode:
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