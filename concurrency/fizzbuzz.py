from threading import Semaphore, Thread
from typing import Callable

from threading import Semaphore, Thread

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1  # Start from 1 and go up to n

        # Semaphores to control which thread can run
        self.sem_number = Semaphore(1)     # number() starts first
        self.sem_fizz = Semaphore(0)       # fizz() waits
        self.sem_buzz = Semaphore(0)       # buzz() waits
        self.sem_fizzbuzz = Semaphore(0)   # fizzbuzz() waits

    def fizz(self, printFizz):
        while True:
            self.sem_fizz.acquire()  # Wait until signaled to print "fizz"
            if self.current > self.n:  # Exit condition
                self._release_all()
                return
            printFizz()  # Print "fizz"
            self.current += 1
            self._release_next()  # Hand control back to number()

    def buzz(self, printBuzz):
        while True:
            self.sem_buzz.acquire()  # Wait until signaled to print "buzz"
            if self.current > self.n:
                self._release_all()
                return
            printBuzz()  # Print "buzz"
            self.current += 1
            self._release_next()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            self.sem_fizzbuzz.acquire()  # Wait until signaled to print "fizzbuzz"
            if self.current > self.n:
                self._release_all()
                return
            printFizzBuzz()  # Print "fizzbuzz"
            self.current += 1
            self._release_next()

    def number(self, printNumber):
        while self.current <= self.n:
            self.sem_number.acquire()  # Only number() is allowed to evaluate
            if self.current % 3 == 0 and self.current % 5 == 0:
                self.sem_fizzbuzz.release()  # Let fizzbuzz() handle it
            elif self.current % 3 == 0:
                self.sem_fizz.release()  # Let fizz() handle it
            elif self.current % 5 == 0:
                self.sem_buzz.release()  # Let buzz() handle it
            else:
                printNumber(self.current)  # Print the number itself
                self.current += 1
                self._release_next()  # Go to the next number

        # Once done, make sure other threads can exit gracefully
        self._release_all()

    def _release_next(self):
        # Always allow number() thread to proceed after any other thread prints
        self.sem_number.release()

    def _release_all(self):
        # In case any thread is still blocked when done, release them
        self.sem_fizz.release()
        self.sem_buzz.release()
        self.sem_fizzbuzz.release()
        self.sem_number.release()


fb = FizzBuzz(30)

# Print functions passed to the threads
def printFizz(): print("fizz")
def printBuzz(): print("buzz")
def printFizzBuzz(): print("fizzbuzz")
def printNumber(x): print(x)

# Creating threads for each role
threads = [
    Thread(target=fb.fizz, args=(printFizz,)),
    Thread(target=fb.buzz, args=(printBuzz,)),
    Thread(target=fb.fizzbuzz, args=(printFizzBuzz,)),
    Thread(target=fb.number, args=(printNumber,))
]

# Start and join all threads
for t in threads: t.start()
for t in threads: t.join()
