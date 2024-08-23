import threading
import time
import queue

CAPACITY = 10
buffer = queue.Queue(CAPACITY)  # Create a queue with a maximum size of CAPACITY

class Producer(threading.Thread):
    def run(self):
        item_produced = 0
        counter = 0

        while item_produced < 20:
            counter += 1
            buffer.put(counter)  # Put item in the queue (blocks if full)
            print("Producer produced:", counter)
            time.sleep(1)  # Simulate time taken to produce an item
            item_produced += 1

class Consumer(threading.Thread):
    def run(self):
        item_consumed = 0

        while item_consumed < 20:
            item = buffer.get()  # Get item from the queue (blocks if empty)
            print("Consumer consumed item:", item)
            time.sleep(2.5)  # Simulate time taken to consume an item
            item_consumed += 1

# Creating producer and consumer threads
producer = Producer()
consumer = Consumer()

# Starting threads
consumer.start()
producer.start()

# Waiting for threads to complete
producer.join()
consumer.join()