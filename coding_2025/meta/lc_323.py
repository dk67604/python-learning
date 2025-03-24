'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

✅ Time Complexity: O(E × α(n))
Where:

n = number of nodes

E = number of edges

α(n) = inverse Ackermann function — grows extremely slowly and is considered constant (≤ 5) in all practical scenarios.

Explanation:
find(x) uses path compression, and union(x, y) uses union by size.

These optimizations ensure that each union or find operation takes amortized O(α(n)) time.

You loop through each edge once → E calls to union().

So total time complexity:
✅ O(E × α(n)), which is practically linear time.

✅ Space Complexity: O(n)
Explanation:

You maintain two arrays:

parent[] of size n

size[] of size n

So total auxiliary space = O(n)
'''

from typing import List

# Union-Find (Disjoint Set) class
class UnionFind:
    def __init__(self, size: int):
        # Initialize each node as its own parent (self-loop)
        self.parent = [i for i in range(size)]
        # Track the size of each connected component
        self.size = [1] * size  

    def union(self, x: int, y: int) -> bool:
        """
        Merges two sets if they are disjoint.
        Returns False if they are already connected (i.e., cycle detected).
        """
        rep_x, rep_y = self.find(x), self.find(y)  # Find representatives (leaders)
        
        if rep_x == rep_y:
            return False  # If both nodes have the same representative, cycle detected

        # Union by size: attach the smaller tree under the larger tree
        if self.size[rep_x] > self.size[rep_y]:
            self.parent[rep_y] = rep_x  # Make rep_x the parent of rep_y
            self.size[rep_x] += self.size[rep_y]  # Update size of the component
        else:
            self.parent[rep_x] = rep_y  # Make rep_y the parent of rep_x
            self.size[rep_y] += self.size[rep_x]  # Update size of the component

        return True  # Successfully merged

        

    def find(self, x: int) -> int:
        """
        Finds the representative (leader) of the set that `x` belongs to.
        Uses **path compression** to flatten the tree, optimizing future queries.
        """
        if x == self.parent[x]:
            return x  # If `x` is its own parent, it is the root
        
        # Path Compression: directly connect node to its root representative
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def size(self, x:int) -> int:
        return self.size[self.find(x)]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for u, v in edges:
            if uf.union(u,v):
                res -=1
        return res
        