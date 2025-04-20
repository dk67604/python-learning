import threading
import time

class RateLimiter:
    def __init__(self, rate: int, capacity: int = 0 ):
        """
        Initializes the RateLimiter.

        :param rate: The rate limit (requests per second).
        :param capacity: The maximum burst size. If None, the capacity is set to the rate.
        """
        self.rate = rate # tokens per second
        self.capacity = capacity or rate # max tokens allowed at once
        self.tokens = 0 #start with full capacity
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.last_refill = time.time()

        # Start a background thread to refill tokens regularly
        self.refill_thread = threading.Thread(target=self._refill_tokens, daemon=True)
        self.refill_thread.start()

    def _refill_tokens(self):
        """
        Background daemon thread that refills tokens based on elapsed time.
        """
        while True:
            time.sleep(0.1) # Check every 100ms
            now = time.time()
            with self.condition:
                elapsed = now - self.last_refill
                added_token = int(elapsed * self.rate)
                if added_token > 0:
                    # Add tokens but not exceed capacity
                    self.tokens = min(self.tokens + added_token, self.capacity)
                    self.last_refill = now
                    #Notify any waiting threads
                    self.condition.notify_all()

    def acquire(self):
        """
        Acquire a token from the rate limiter. Blocks until a token is available.
        """
        with self.condition:
            while self.tokens <=0:
                # Wait for a token to be available
                self.condition.wait()
            # Consume a token
            self.tokens -= 1
            # You now have permission to proceed

def worker(rate_limiter: RateLimiter, thread_id: int):
    """Rate limiter worker function.
    This function simulates a thread that needs to acquire a token from the rate limiter
    before proceeding with its task.

    Args:
        rate_limiter (RateLimiter): Thread-safe rate limiter instance.
        thread_id (int): Thread ID for logging purposes.
    """

    for i in range(3):
        rate_limiter.acquire()
        print(f"Thread {thread_id} doing task {i} at {time.time():.2f}")
        time.sleep(0.2) # Simulate some work

def main():

    limiter = RateLimiter(rate=5)
    threads = []
    # Start 3 worker threads
    for i in  range(3):
        t = threading.Thread(target=worker, args=(limiter, i))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()
    print("All tasks completed.")

if __name__ == "__main__":
    main()