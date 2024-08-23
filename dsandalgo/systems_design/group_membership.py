import threading
import time
import random

class Node:
    def __init__(self, node_id, membership_list):
        self.node_id = node_id
        self.membership_list = membership_list
        self.lock = threading.Lock()

    def gossip(self):
        while True:
            with self.lock:
                if len(self.membership_list) > 1:
                    target_node_id = random.choice(self.membership_list)
                    if target_node_id != self.node_id:
                        print(f"Node {self.node_id} gossiping with Node {target_node_id}")
                        # Simulate gossip by copying membership_list
                        target_node = nodes[target_node_id]
                        with target_node.lock:
                            target_node.membership_list = list(set(target_node.membership_list) | set(self.membership_list))
            time.sleep(random.uniform(1, 3))

    def join(self, new_node_id):
        with self.lock:
            self.membership_list.append(new_node_id)

    def leave(self, node_id):
        with self.lock:
            if node_id in self.membership_list:
                self.membership_list.remove(node_id)
def simulate():
    global nodes
    nodes = {}

    # Create initial nodes
    for i in range(5):
        nodes[i] = Node(i, [i])

    # Start gossiping
    for node in nodes.values():
        t = threading.Thread(target=node.gossip)
        t.start()

    # Simulate node join
    time.sleep(5)
    new_node_id = 3
    nodes[new_node_id] = Node(new_node_id, [new_node_id])
    for node in nodes.values():
        node.join(new_node_id)
    print(f"Node {new_node_id} joined")

    # Simulate node leave
    time.sleep(10)
    leaving_node_id = 2
    for node in nodes.values():
        node.leave(leaving_node_id)
    print(f"Node {leaving_node_id} left")

if __name__ == "__main__":
    simulate()