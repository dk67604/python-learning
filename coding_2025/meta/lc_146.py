'''
https://leetcode.com/problems/lru-cache/description/

✅ Time Complexity:
get(key) → O(1)

put(key, value) → O(1)

Explanation:
Both get and put operations perform:

Hashmap lookups (e.g., self.hashmap[key]) → O(1)

Doubly Linked List operations (add_to_tail, remove_node) → O(1) because they only involve pointer adjustments.

So, every operation (get/put) completes in constant time → O(1).

This is the key design of an efficient LRU cache: combining a hashmap (for fast lookup) and a doubly linked list (for tracking usage order in constant time).

✅ Space Complexity: O(capacity)
Explanation:

The cache stores up to capacity nodes.

Each node is stored in both:

the hashmap (for key lookup),

and the doubly linked list (for usage ordering).

Therefore, space grows linearly with capacity.

🧠 Summary:
Operation	Time Complexity
get()	O(1)
put()	O(1)
Space Complexity: O(capacity)

Let me know if you'd like a visual diagram of how get and put work step-by-step!
'''
# Node definition for a doubly linked list
class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key                      # Store key for hashmap reference
        self.val = val                      # Value associated with the key
        self.next = self.prev = None        # Pointers for DLL navigation

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity            # Maximum number of entries in cache
        self.hashmap = {}                   # Hashmap to store key → node mapping for O(1) access
        # Create dummy head and tail nodes to simplify insert/remove logic
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node) -> None:
        """
        Add the given node just before the tail (most recently used position).
        """
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node) -> None:
        """
        Disconnect the node from the doubly linked list.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        """
        Return the value associated with the key if it exists.
        Move the node to the tail to mark it as recently used.
        """
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self.remove_node(node)     # ✅ Remove from current position in DLL
        self.add_to_tail(node)     # ✅ Re-add to tail as most recently used
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.
        If the key exists, update and move it to tail.
        If the cache exceeds capacity, evict the least recently used node.
        """
        if key in self.hashmap:
            # ✅ Remove the existing node before inserting the updated one
            self.remove_node(self.hashmap[key])
            del self.hashmap[key]

        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node
        # If the cache is over capacity, remove the least recently used node (head.next)
        if len(self.hashmap) > self.capacity:
            lru_node = self.head.next
            self.remove_node(lru_node)          # Remove from DLL
            del self.hashmap[lru_node.key]      # Remove from hashmap

        self.add_to_tail(node)