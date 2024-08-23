"""
t.start()
Purpose: The start() method is used to begin the execution of a thread.

How It Works:

When you call t.start() on a thread object t, it invokes the thread's run() method in a separate thread of execution.
The start() method does not block the main thread. This means that after starting a thread with t.start(), the main program (or any other thread) continues its execution concurrently with the newly started thread.
It's important to note that you should only call start() once per thread object. Calling start() more than once on the same thread will raise a RuntimeError.

t.join()
Purpose: The join() method is used to wait for a thread to complete its execution before continuing with the execution of the calling thread.

How It Works:

When you call t.join() on a thread object t, the calling thread (typically the main thread) will pause its execution and wait for thread t to finish.
Once thread t has completed its task, the join() method returns, and the calling thread resumes execution.
join() is particularly useful when you want to ensure that a thread has completed its work before the program continues or exits.
"""
import threading
import time


def worker():
    print("Worker thread is starting")
    time.sleep(2)
    print("Worker thread is done")

t = threading.Thread(target=worker)
t.start()
print("Main thread is waiting for worker thread to finish")
t.join()  # Wait for the worker thread to finish
print("Worker thread has finished, main thread continues")
