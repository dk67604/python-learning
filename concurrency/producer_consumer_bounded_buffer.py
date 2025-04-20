'''
✅ Correct Flow:
Start all consumers first (so they’re ready).

Start all producers.

Wait for all producers to join() — i.e., finish producing.

Put None sentinels into queue to tell consumers to stop.

Wait for consumers to join().

This guarantees:

All real items are produced and enqueued before any consumer is told to stop.

Consumers only exit after all real work is done.
'''
import queue
import threading
import random
import time
class Item:
    def __init__(self, value):
        self.value = value

def producer(buffer, n):
    for _ in range(n):
        item = Item(random.randint(1, 100))
        buffer.put(item)
        print(f'Produced {item.value}')
        time.sleep(0.1)

def consumer(buffer):
    while True:
        item = buffer.get()
        if item is None:
            print('Consumer received None, stopping.')
            buffer.task_done()
            break
        print(f'Consumed {item.value}')
        buffer.task_done()

def main():
    n_producers = 2
    item_by_per_producer = 5

    buffer_size = 10
    buffer = queue.Queue(maxsize=buffer_size)

    n_consumers = 3
    threads = []
    for i in range(n_consumers):
        t = threading.Thread(target=consumer, args=(buffer,))
        threads.append(t)
        t.start()

    for i in range(n_producers):
        t = threading.Thread(target=producer, args=(buffer, item_by_per_producer))
        threads.append(t)
        t.start()


    # Wait for all producers to finish

    for t in threads[n_consumers:]:
        t.join()
    # Stop consumers
    for _ in range(n_consumers):
        buffer.put(None)
        print('Sent None to consumer.')

    # Wait for consumers to finish
    for t in threads[:n_consumers]:
        t.join()


if __name__ == '__main__':
    main()
    print('Main thread finished.')