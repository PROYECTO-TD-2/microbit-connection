from microbit import microphone
from sensor_strategy import SensorStrategy

class SensorSonido(SensorStrategy):
    def read(self):
        # Devuelve el nivel de sonido en rango 0–255
        nivel = microphone.sound_level()
        pendiente = 0.204
        intercepto = 62.8039
        return (nivel * pendiente) + intercepto
