from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore(1)
        self.bar_sem = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foo_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sem.release()