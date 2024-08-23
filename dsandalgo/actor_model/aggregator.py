import pykka
from typing import Dict

class Aggregator(pykka.ThreadingActor):
    def __init__(self) -> None:
        super().__init__()
        self.total_temperature = 0
        self.reading_count = 0

    def on_receive(self, message: Dict[str, int]) -> None:
        if 'temperature' in message:
            temperature = message['temperature']
            self.total_temperature += temperature
            self.reading_count += 1
            average_temperature = self.total_temperature / self.reading_count
            print(f"Received temperature: {temperature}°C, Average: {average_temperature:.2f}°C")
