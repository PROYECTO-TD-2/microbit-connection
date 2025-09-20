from microbit import *
import radio

# Importar sensores
from sensor_temperatura import SensorTemperatura
from sensor_luz import SensorLuz
from sensor_acelerometro import SensorAcelerometro
from sensor_sonido import SensorSonido

radio.on()
radio.config(group=1, power=7)

# Registro de estrategias disponibles
strategies = {
    "temperatura": SensorTemperatura(),
    "luz": SensorLuz(),
    "acelerometro": SensorAcelerometro(),
    "sonido": SensorSonido()
}

# Variable de sensor activo
active_sensor = None

while True:
    # --- Recepción por radio ---
    msg = radio.receive()
    if msg:
        display.show(Image.YES)
        sleep(500)
        display.clear()

        # Buscar sensor en strategies
        msg_lower = msg.lower()
        if msg_lower in strategies:
            active_sensor = strategies[msg_lower]
            display.show(Image.HAPPY)
        else:
            active_sensor = None
            display.show(Image.NO)

    # --- Detección y envío de datos ---
    if active_sensor and button_a.was_pressed():
        values = []
        detectando = True
        while detectando:
            if button_a.was_pressed():
                val = active_sensor.read()
                display.scroll(str(val))
                values.append(val)

            if button_b.was_pressed():
                detectando = False

        # Envío por radio
        radio.send(str(values))
        display.show(Image.TARGET)
        display.clear()
        active_sensor = None