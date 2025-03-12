class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        def dfs(node:int, color: int) -> bool:
            nonlocal colors
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if (colors[neighbor] == 0 and not dfs(neighbor, -color)):
                    return False
            return True

        for i in range(len(graph)):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True

        