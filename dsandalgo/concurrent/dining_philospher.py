import threading
import time
import random

class Philospher(threading.Thread):

    def __init__(self, id, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork

    def think(self):
        print(f"Philosopher {self.id} is thinking.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate thinking

    def eat(self):
        print(f"Philosopher {self.id} is eating.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate eating


    def run(self):
        for _ in range(10):
            self.think()

            if self.id % 2 == 0:
                self.right_fork.acquire()
                self.left_fork.acquire()
            else:
                self.left_fork.acquire()
                self.right_fork.acquire()

            self.eat()

            self.left_fork.release()
            self.right_fork.release()

            time.sleep(random.uniform(0.1, 0.5))

def main():
    num_philosphers = 5
    forks = [threading.Lock() for _ in range(num_philosphers)]
    philoshpers = []

    for i in range(num_philosphers):
        left_fork = forks[i]
        right_fork = forks[(i+1) % num_philosphers]
        philoshper = Philospher(i,left_fork,right_fork)
        philoshpers.append(philoshper)
        philoshper.start()

    for philoshper in philoshpers:
        philoshper.join()

if __name__ == "__main__":
    main()
