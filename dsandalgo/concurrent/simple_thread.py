import time
import threading

def task():
    time.sleep(1)
    print('All done in the new thread')

thread  = threading.Thread(target=task)
thread.start()
# wait for the new thread to finish
print('Main: Waiting for thread to terminate...')
thread.join()
# continue on
print('Main: Continuing on')
