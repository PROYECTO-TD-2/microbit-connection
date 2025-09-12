from microbit import temperature
from sensor_strategy import SensorStrategy

class SensorTemperatura(SensorStrategy):
    def read(self):
        return temperature()
