from threading import Thread
from typing import Callable
import threading
import random

class H2O:
    def __init__(self):
        self.h_sem = threading.Semaphore(2)  # Two hydrogens
        self.o_sem = threading.Semaphore(1)  # One oxygen
        self.barrier = threading.Barrier(3)  # Wait for 3 threads total

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()                 # Try to be one of two hydrogens
        self.barrier.wait()                  # Wait for molecule to be complete
        releaseHydrogen()
        self.h_sem.release()                 # Make room for next hydrogen

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()                 # Try to be the oxygen
        self.barrier.wait()                  # Wait for molecule to be complete
        releaseOxygen()
        self.o_sem.release()                 # Make room for next oxygen


def releaseHydrogen():
    print("H", end='')

def releaseOxygen():
    print("O", end='')

h2o = H2O()

atoms = ['H', 'H', 'O', 'H', 'H', 'O']  # Represents HHOHHO

threads = []
for atom in atoms:
    if atom == 'H':
        t = Thread(target=h2o.hydrogen, args=(releaseHydrogen,))
    else:
        t = Thread(target=h2o.oxygen, args=(releaseOxygen,))
    threads.append(t)

random.shuffle(threads)  # Simulate arrival in any order
for t in threads: t.start()
for t in threads: t.join()
