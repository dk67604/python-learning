from threading import Condition
from typing import Callable


class DiningPhilosophers:
    def __init__(self):
        self.condition = Condition()
        self.fork_in_use = [False] * 5  # Five forks, initially not in use

    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]', pickRightFork: 'Callable[[], None]', eat: 'Callable[[], None]', putLeftFork: 'Callable[[], None]', putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        with self.condition:
            # Wait until both forks are available
            while self.fork_in_use[left] or self.fork_in_use[right]:
                self.condition.wait()

            # Pick up the forks
            self.fork_in_use[left] = True
            self.fork_in_use[right] = True
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()

            with self.condition:
                # Put down the forks
                self.fork_in_use[left] = False
                self.fork_in_use[right] = False
                self.condition.notify_all()

from threading import Thread
import time, random

def simulate(philosopher_id, dp):
    for _ in range(2):  # Eat twice
        time.sleep(random.uniform(0.1, 0.5))  # Thinking
        dp.wantsToEat(
            philosopher_id,
            lambda: print(f"{philosopher_id} picked left"),
            lambda: print(f"{philosopher_id} picked right"),
            lambda: print(f"{philosopher_id} is eating 🍝"),
            lambda: print(f"{philosopher_id} put left"),
            lambda: print(f"{philosopher_id} put right")
        )

dp = DiningPhilosophers()
threads = [Thread(target=simulate, args=(i, dp)) for i in range(5)]

for t in threads: t.start()
for t in threads: t.join()
