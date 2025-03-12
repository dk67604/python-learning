class GraphNode:
    def __init__(self, val):
        """
        Initializes a graph node with a value and an empty list of neighbors.
        """
        self.val = val
        self.neighbors = []  # List to store adjacent nodes

def graph_deep_copy(node: GraphNode) -> GraphNode:
    """
    Creates a deep copy of a given graph using Depth-First Search (DFS).
    
    Args:
        node (GraphNode): The starting node of the graph.

    Returns:
        GraphNode: The root of the newly cloned graph.
    """
    if not node:
        return None  # If the input node is None, return None
    
    return dfs(node)  # Start DFS traversal to clone the graph

def dfs(node: GraphNode, clone_map={}) -> GraphNode:
    """
    Performs a DFS-based deep copy of the graph.

    Args:
        node (GraphNode): The current node being cloned.
        clone_map (dict): A dictionary to store visited nodes and their clones.

    Returns:
        GraphNode: The cloned node.
    """
    # If the node is already cloned, return the cloned version
    if node in clone_map:
        return clone_map[node]

    # Step 1: Create a new node (clone) with the same value as the original
    cloned_node = GraphNode(node.val)

    # Step 2: Store the cloned node in the dictionary to avoid duplication
    clone_map[node] = cloned_node

    # Step 3: Recursively clone all the neighbors
    for neighbor in node.neighbors:
        cloned_neighbor = dfs(neighbor, clone_map)  # Recursive DFS call
        cloned_node.neighbors.append(cloned_neighbor)  # Add the cloned neighbor to the new node

    return cloned_node  # Return the cloned node
