import random
import time
import pykka

class Sensor(pykka.ThreadingActor):
    def __init__(self, sensor_id, aggregator, max_readings=10):
        super().__init__()
        self.sensor_id = sensor_id
        self.aggregator = aggregator
        self.max_readings = max_readings

    def send_temperature(self):
        for _ in range(self.max_readings):
            temperature = random.uniform(20, 30)  # Generate a random temperature between 20 and 30°C
            print(f"Sensor {self.sensor_id} sending temperature: {temperature:.2f}°C")
            self.aggregator.tell({'temperature': temperature})
            time.sleep(random.uniform(0.5, 2))  # Simulate delay between readings

        print(f"Sensor {self.sensor_id} completed its readings.")