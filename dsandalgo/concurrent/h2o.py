import threading
from typing import Callable
class H2O:
    def __init__(self) -> None:
        self.hydrogen_semaphore = threading.Semaphore(2)
        self.oxygen_semaphore = threading.Semaphore(1)
        self.barrier = threading.Barrier(3)
        self.mutex = threading.Lock()
        self.hydrogen_count = 0
        self.oxygen_count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_semaphore.acquire()

        with self.mutex:
            self.hydrogen_count +=1

        self.barrier.wait()

        releaseHydrogen()

        with self.mutex:
            self.hydrogen_count -= 1
            if self.hydrogen_count == 0 and self.oxygen_count == 0:
                self.hydrogen_semaphore.release()
                self.hydrogen_semaphore.release()
                self.oxygen_semaphore.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_semaphore.acquire()
        with self.mutex:
            self.oxygen_count += 1

        self.barrier.wait()

        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()

        with self.mutex:
            self.oxygen_count -= 1
            if self.hydrogen_count == 0 and self.oxygen_count == 0:
                # Reset the semaphores for the next molecule
                self.hydrogen_semaphore.release()
                self.hydrogen_semaphore.release()
                self.oxygen_semaphore.release()
