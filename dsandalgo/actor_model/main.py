from aggregator import Aggregator
from sensor import Sensor
import time
if __name__ == "__main__":
    # Start the aggregator actor
    aggregator = Aggregator.start()

    # Start multiple sensor actors
    sensors = [Sensor.start(sensor_id=i, aggregator=aggregator) for i in range(5)]

    # Start sending temperature readings concurrently
    for sensor in sensors:
        sensor.proxy().send_temperature()

    # Run for a while to gather readings
    time.sleep(10)

    # Stop all actors
    for sensor in sensors:
        sensor.stop()
    aggregator.stop()