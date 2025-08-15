from microbit import *
import radio

# Activamos el radio
radio.on()
radio.config(group=1)  # Debe coincidir con el grupo del emisor

while True:
    sensor_type = radio.receive()
    if sensor_type:
        display.show(Image.YES)
        display.scroll(str(sensor_type))