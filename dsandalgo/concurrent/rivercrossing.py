import threading

class Boat:
    def __init__(self):
        self.hackers = 0
        self.serfs = 0
        self.lock = threading.Lock()
        self.boarding_barrier = threading.Barrier(4)
        self.hacker_sem = threading.Semaphore(0)
        self.serf_sem = threading.Semaphore(0)
        self.row_sem = threading.Semaphore(0)

    def hacker(self, board: 'Callable[[], None]') -> None:
        with self.lock:
            self.hackers += 1
            if self.hackers == 4:
                # Allow 4 hackers to board
                self.hacker_sem.release(4)
                self.hackers -= 4
                self.row_sem.release()
            elif self.hackers == 2 and self.serfs >= 2:
                # Allow 2 hackers and 2 serfs to board
                self.hacker_sem.release(2)
                self.serf_sem.release(2)
                self.hackers -= 2
                self.serfs -= 2
                self.row_sem.release()
            else:
                # Exit the critical section if conditions don't match
                self.lock.release()
                self.hacker_sem.acquire()
                return

        self.hacker_sem.acquire()
        self.board(board)

    def serf(self, board: 'Callable[[], None]') -> None:
        with self.lock:
            self.serfs += 1
            if self.serfs == 4:
                # Allow 4 serfs to board
                self.serf_sem.release(4)
                self.serfs -= 4
                self.row_sem.release()
            elif self.serfs == 2 and self.hackers >= 2:
                # Allow 2 serfs and 2 hackers to board
                self.serf_sem.release(2)
                self.hacker_sem.release(2)
                self.serfs -= 2
                self.hackers -= 2
                self.row_sem.release()
            else:
                # Exit the critical section if conditions don't match
                self.lock.release()
                self.serf_sem.acquire()
                return

        self.serf_sem.acquire()
        self.board(board)

    def board(self, board: 'Callable[[], None]') -> None:
        # Perform the boarding action (e.g., print a message)
        board()

        # Wait at the barrier until all four threads have called board()
        self.boarding_barrier.wait()

        # Only one thread should call rowBoat after all threads are boarded
        if self.boarding_barrier.n_waiting == 0:
            self.row_sem.acquire()
            self.rowBoat()

    def rowBoat(self) -> None:
        print(f"{threading.current_thread().name} is rowing the boat!")

def board():
    print(f"{threading.current_thread().name} is boarding the boat.")

def hacker_thread(boat: Boat):
    boat.hacker(board)

def serf_thread(boat: Boat):
    boat.serf(board)

def main():
    boat = Boat()

    # Create threads for hackers and serfs
    threads = []
    for i in range(10):
        if i % 2 == 0:
            t = threading.Thread(target=hacker_thread, args=(boat,))
        else:
            t = threading.Thread(target=serf_thread, args=(boat,))
        t.setName(f"Hacker-{i//2}" if i % 2 == 0 else f"Serf-{i//2}")
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
