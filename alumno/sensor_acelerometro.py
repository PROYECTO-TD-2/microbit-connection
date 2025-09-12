from microbit import accelerometer
from sensor_strategy import SensorStrategy

class SensorAcelerometro(SensorStrategy):
    def read(self):
        # Retorna una tupla con los valores x, y, z
        return (accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z())
