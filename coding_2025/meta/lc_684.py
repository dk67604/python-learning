'''
https://leetcode.com/problems/redundant-connection/description/

✅ Time Complexity: O(n * α(n))
Where:

n is the number of nodes (or edges, since this is a connected graph)

α(n) is the inverse Ackermann function, which grows extremely slowly and is practically constant for all realistic values of n (even up to billions)

Why?
You loop through each of the n edges → O(n)

Each call to union() involves two find() operations

With path compression, each find() takes O(α(n))

So each union takes O(α(n)) in the worst case

➡️ Total = O(n * α(n)) → considered almost linear

✅ Space Complexity: O(n)
The Union-Find structure uses:

parent[] array of size n + 1

size[] array of size n + 1

So the overall space used is O(n)
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

# Main solution class
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the redundant edge in a given undirected graph that, if removed,
        results in a tree (i.e., an acyclic connected graph).
        """
        size = len(edges) + 1  # Total nodes (1-based indexing)
        union_find = UnionFind(size)  # Initialize Union-Find structure

        for n1, n2 in edges:
            # If the union operation fails, it means this edge creates a cycle
            if not union_find.union(n1, n2):
                return [n1, n2]  # Return the redundant edge
        
        return []  # Default return (should never reach this point)
