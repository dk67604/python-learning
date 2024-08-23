import time
import threading
import random


# reporting function
def report(lock,identifier):
    with lock:
        print(f'>thread {identifier} done')

# work function
def task(lock, identifier, value):
    #acuire lock
    with lock:
        print(f'>thread {identifier} sleeping for {value}')
        time.sleep(value)
        #report
        report(lock=lock, identifier=identifier)

lock = threading.RLock()
threads = [threading.Thread(target=task, args=(lock, i, random.random())) for i in range(10)]
for t in threads:
    t.start()