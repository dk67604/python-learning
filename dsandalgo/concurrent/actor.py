import queue
import threading
import time

class Actor:
    def __init__(self):
        self.mailbox = queue.Queue()
        self._stop_event = threading.Event()

    def send(self, message):
        self.mailbox.put(message)

    def stop(self):
        self._stop_event.set()

    def run(self):
        while not self._stop_event.is_set():
            try:
                message = self.mailbox.get(timeout=1)
                self.receive(message)
            except queue.Empty:
                continue

    def receive(self, message):
        raise NotImplementedError("This method should be overridden by subclasses")

    def start(self):
        threading.Thread(target=self.run).start()

class PrintActor(Actor):
    def receive(self, message):
        print(f"Received: {message}")

class SumActor(Actor):
    def __init__(self):
        super().__init__()
        self.total = 0

    def receive(self, message):
        if isinstance(message, int):
            self.total += message
            print(f"Current sum: {self.total}")
        else:
            print(f"Unknown message: {message}")

if __name__ == "__main__":
    print_actor = PrintActor()
    sum_actor = SumActor()

    print_actor.start()
    sum_actor.start()

    print_actor.send("Hello, Actor Model!")
    sum_actor.send(10)
    sum_actor.send(20)
    sum_actor.send("Not an integer")

    time.sleep(2)  # Give the actors some time to process messages

    print_actor.stop()
    sum_actor.stop()
