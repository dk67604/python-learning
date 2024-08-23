import random
import threading
import time

class Node:
    def __init__(self, node_id, neighbors):
        self.node_id = node_id
        self.neighbors = neighbors
        self.received_messages = set()
        self.lock = threading.Lock()
        self.infected = False

    def send_message(self, message, cycle_count):
        with self.lock:
            if message not in self.received_messages:
                print(f"Node {self.node_id} received message: {message}")
                self.received_messages.add(message)
                self.infected = True
                # Forward the message to random neighbors
                self.gossip(message, cycle_count)

    def gossip(self, message, cycle_count):
        selected_neighbors = random.sample(self.neighbors, random.randint(1, len(self.neighbors)))
        for neighbor in selected_neighbors:
            threading.Thread(target=neighbor.send_message, args=(message, cycle_count)).start()

def start_gossip(node, message):
    node.send_message(message, 1)

def all_nodes_infected(nodes):
    return all(node.infected for node in nodes)

def run_simulation(nodes):
    cycle_count = 0
    while not all_nodes_infected(nodes):
        cycle_count += 1
        for node in nodes:
            if node.infected:
                node.gossip("Hello World!", cycle_count)
        time.sleep(1)  # Simulate time delay for each cycle
    return cycle_count

# Create nodes
node_A = Node("A", [])
node_B = Node("B", [])
node_C = Node("C", [])
node_D = Node("D", [])
node_E = Node("E", [])

# Define neighbors (connections between nodes)
node_A.neighbors = [node_B, node_C]
node_B.neighbors = [node_A, node_C, node_D]
node_C.neighbors = [node_A, node_B, node_D, node_E]
node_D.neighbors = [node_B, node_C, node_E]
node_E.neighbors = [node_C, node_D]

# Start the gossip from node A
threading.Thread(target=start_gossip, args=(node_A, "Hello World!")).start()

# Run the simulation
nodes = [node_A, node_B, node_C, node_D, node_E]
cycles = run_simulation(nodes)
print(f"All nodes got infected in {cycles} cycles.")
