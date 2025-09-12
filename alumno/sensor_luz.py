from microbit import display, Image
from sensor_strategy import SensorStrategy

class SensorLuz(SensorStrategy):
    def read(self):
        # truco: contar LEDs encendidos como proxy de luz
        # (micro:bit no tiene sensor de luz directo, se simula con la pantalla)
        level = display.read_light_level()
        return level
