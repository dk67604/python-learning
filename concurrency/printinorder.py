import threading
from typing import Callable
class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.condition = threading.Condition()

    def wait(self):
        with self.condition:
            while self.count > 0:
                self.condition.wait()

    def count_down(self):
        with self.condition:
            if self.count > 0:
                self.count -= 1
                print(f"[Latch] Count is now {self.count}")
                if self.count == 0:
                    self.condition.notify_all()

class Foo:
    def __init__(self):
        self.latch1 = CountDownLatch(1)
        self.latch2 = CountDownLatch(1)

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.latch1.count_down()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.latch1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.latch2.count_down()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.latch2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

from threading import Thread
import time, random

def printFirst(): print("first", end='')
def printSecond(): print("second", end='')
def printThird(): print("third", end='')

foo = Foo()

t1 = Thread(target=lambda: foo.first(printFirst))
t2 = Thread(target=lambda: foo.second(printSecond))
t3 = Thread(target=lambda: foo.third(printThird))

# Random start to simulate disorder
threads = [t1, t2, t3]
random.shuffle(threads)
for t in threads: t.start()
for t in threads: t.join()
