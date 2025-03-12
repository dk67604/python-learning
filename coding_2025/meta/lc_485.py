'''
785. Is Graph Bipartite?
Solved
Medium
Topics
Companies
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

 

Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
Seen this question in a real interview before?
1/5
'''

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Array to store colors of nodes: 0 (unvisited), 1 (color A), -1 (color B)
        colors = [0] * len(graph)
        
        # Depth-First Search (DFS) function to check bipartiteness
        def dfs(node: int, color: int) -> bool:
            nonlocal colors
            # Color the current node
            colors[node] = color
            
            # Check all neighbors
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    # Conflict detected: neighbor has the same color
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    # If unvisited, recursively apply DFS with opposite color
                    return False
            
            return True

        # Loop through each node to ensure all components are checked
        for i in range(len(graph)):
            if colors[i] == 0:  # If the node is unvisited, start DFS
                if not dfs(i, 1):  # Try to color with 1, if fails return False
                    return False
        
        return True  # If no conflicts found, the graph is bipartite

        