import heapq
from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def combine_sorted_linked_list(lists: List[ListNode]) -> ListNode:
    """
    Merges multiple sorted linked lists into a single sorted linked list using a min heap.

    :param lists: A list of ListNode objects, each representing a sorted linked list.
    :return: The head of the merged sorted linked list.
    """

    heap = []

    # Override the less-than operator for ListNode so heapq knows how to compare nodes
    ListNode.__lt__ = lambda self, other: self.val < other.val

    # Push the head of each non-empty linked list into the min heap
    for head in lists:
        if head:
            heapq.heappush(heap, head)

    # Dummy node to simplify result list construction
    dummy = ListNode(-1)
    curr = dummy

    # While there are elements in the heap
    while heap:
        # Pop the smallest node from the heap
        smallest_node = heapq.heappop(heap)

        # Append it to the result list
        curr.next = smallest_node
        curr = curr.next

        # If there is a next node in the list, push it into the heap
        if smallest_node.next:
            heapq.heappush(heap, smallest_node.next)

    # Return the merged linked list (skipping dummy)
    return dummy.next
