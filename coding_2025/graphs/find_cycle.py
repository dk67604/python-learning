'''
Directed Graph
'''

from collections import defaultdict

WHITE, GRAY, BLACK = 0, 1,2

def has_cycle(graph):
    color = defaultdict(lambda: WHITE)

    def dfs(node):
        if color[node] == GRAY:
            return True
        if color[node] == BLACK:
            return False

        color[node] = GRAY

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        color[node] = BLACK
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False




def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Back edge found (cycle)
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False
