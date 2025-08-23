from microbit import *
import radio

radio.on()
radio.config(group=1)

# Variable para guardar si hay que enviar temperatura
enviar_temperatura = False

while True:
    # --- Recepción por radio ---
    msg = radio.receive()
    if msg:
        display.show(Image.YES)
        sleep(500)
        display.clear()

        parts = msg.split("|")
        if len(parts) == 3:
            sensor, premisa, nivel = parts
            display.scroll("Sensor:" + sensor)
            display.scroll("Nivel:" + nivel)

            # Si el sensor es temperatura, activamos flag
            if sensor.lower() == "temperatura":
                
                enviar_temperatura = True
            else:
                enviar_temperatura = False
        else:
            display.scroll(msg)  # fallback si el formato no coincide

    # --- Botón A para enviar temperatura ---
    if enviar_temperatura and button_a.is_pressed():
        temp = temperature()  # función de micro:bit que devuelve temperatura en °C
        radio.send(str(temp))
        display.show(Image.TARGET)
        sleep(500)
        display.clear()
        enviar_temperatura = False  # solo enviamos una vez por presión
