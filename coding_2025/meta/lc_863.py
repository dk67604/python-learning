'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
from collections import defaultdict, deque
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Finds all nodes that are exactly `k` distance away from the target node in a binary tree.
        
        :param root: The root of the binary tree.
        :param target: The target node whose distance-k neighbors are to be found.
        :param k: Distance from the target node.
        :return: A list of node values that are exactly `k` distance from the target node.
        """

        # Step 1: Convert the Binary Tree into an Undirected Graph
        graph = defaultdict(list)  # Adjacency list representation of the tree

        def build_graph(cur: TreeNode, parent: TreeNode):
            """
            Constructs an adjacency list from the binary tree.
            This allows bidirectional traversal between parent and child nodes.
            
            :param cur: The current node in the tree.
            :param parent: The parent node of `cur`.
            """
            if not cur:
                return

            if parent:
                graph[cur.val].append(parent.val)  # Add parent connection
                graph[parent.val].append(cur.val)  # Add child connection

            # Recursively build the graph for left and right subtrees
            build_graph(cur.left, cur)
            build_graph(cur.right, cur)

        # Build the graph starting from the root node
        build_graph(root, None)

        # Step 2: BFS Traversal from Target Node
        answer = []  # Stores nodes at exactly `k` distance
        visited = set([target.val])  # Set to track visited nodes
        queue = deque([(target.val, 0)])  # BFS queue initialized with (target, distance)

        while queue:
            cur, distance = queue.popleft()

            # If the current node is exactly `k` distance away, add it to the answer list
            if distance == k:
                answer.append(cur)
                continue  # No need to explore further from this node
            
            # Explore all neighbors (children and parent)
            for neighbor in graph[cur]:
                if neighbor not in visited:  # Avoid revisiting nodes
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))  # Move to next level

        # Step 3: Return the collected nodes at distance `k`
        return answer
