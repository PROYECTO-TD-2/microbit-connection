from microbit import *

# Lista de imágenes del reloj
clock_images = [
    Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7,
    Image.CLOCK6, Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1
]

NUM_POSITIONS = len(clock_images)
position = 0  # Posición inicial (0–10)

# Pines del encoder (ajusta según tu conexión)
pinA = pin0
pinB = pin1

# Estado anterior de A
lastA = pinA.read_digital()

display.show(clock_images[position])

while True:
    # Leer pin A actual
    currentA = pinA.read_digital()

    # Detectar flanco (cuando A cambia)
    if currentA != lastA:
        # Verificar dirección según el estado de B
        if pinB.read_digital() != currentA:
            # Giro horario (derecha)
            position = (position + 1) % NUM_POSITIONS
        else:
            # Giro antihorario (izquierda)
            position = (position - 1) % NUM_POSITIONS

        display.show(clock_images[position])
        sleep(10)  # Pequeño debounce

    lastA = currentA


    sleep(1)
