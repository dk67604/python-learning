from threading import Semaphore, Thread
from typing import Callable

class ZeroEvenOdd:
    def __init__(self, n: int) -> None:
        self.n = n
        self.counter = 1
        self.sum_zero = Semaphore(1)
        self.sum_even = Semaphore(0)
        self.sum_odd = Semaphore(0)

    def zero(self, printZero: Callable[[int], None]) -> None:
        for _ in range(self.n):
            self.sum_zero.acquire()
            printZero(0)
            if self.counter % 2 == 0:
                self.sum_even.release()
            else:
                self.sum_odd.release()

    def even(self, printEven: Callable[[int], None]) -> None:
        for _ in range(2, self.n + 1, 2):
            self.sum_even.acquire()
            printEven(self.counter)
            self.counter += 1
            self.sum_zero.release()

    def odd(self, printOdd: Callable[[int], None]) -> None:
        for _ in range(1, self.n + 1, 2):
            self.sum_odd.acquire()
            printOdd(self.counter)
            self.counter += 1
            self.sum_zero.release()