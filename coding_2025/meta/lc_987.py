'''
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Let n be the number of nodes in the binary tree.

1. BFS Traversal:
Each node is visited once → O(n)

2. Appending to column_map:
Each node appends a tuple to a column list → O(1) per node → total O(n)

3. Sorting Columns:
Worst case: all nodes are in one column → sort n items: O(n log n)

In general: sum of all k log k across columns is bounded by O(n log n)

4. Building Result:
Extracting values from each sorted column: O(n)

✅ Total Time Complexity:
O(n log n) — due to sorting the rows within each column

🧮 Space Complexity Analysis:
column_map: stores each node once → O(n)

queue: stores nodes during BFS → up to O(n) in worst case

result: final output with all node values → O(n)

✅ Total Space Complexity:
O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store column index -> list of (row, value)
        column_map = defaultdict(list)

        # Track leftmost and rightmost column indices
        leftmost_column = rightmost_column = 0

        # BFS queue: (node, row, column)
        queue = deque([(root, 0, 0)])

        # Perform BFS traversal while tracking (row, col)
        while queue:
            node, row, column = queue.popleft()

            # Append (row, value) into the corresponding column list
            column_map[column].append((row, node.val))

            # Update column boundaries
            leftmost_column = min(leftmost_column, column)
            rightmost_column = max(rightmost_column, column)

            # Queue left child with updated row and column
            if node.left:
                queue.append((node.left, row + 1, column - 1))

            # Queue right child with updated row and column
            if node.right:
                queue.append((node.right, row + 1, column + 1))

        # Step 2: Extract and sort values from column_map
        result = []

        for col in range(leftmost_column, rightmost_column + 1):
            # Sort first by row, then by value
            sorted_column = sorted(column_map[col])
            # Extract just the values from sorted (row, value) pairs
            result.append([val for row, val in sorted_column])

        return result
