from microbit import *
import radio

radio.on()
radio.config(group=1, power=7)

# Variable para guardar si hay que enviar temperatura
enviar_temperatura = False

while True:
    # --- Recepción por radio ---
    msg = radio.receive()
    if msg:
        display.show(Image.YES)
        sleep(500)
        display.clear()

        if msg:
            display.show(Image.HAPPY)
            
            # Si el sensor es temperatura, activamos flag
            if msg.lower() == "temperatura":
                
                enviar_temperatura = True
            else:
                enviar_temperatura = False
        else:
            display.scroll(msg)  # fallback si el formato no coincide

    values = []
    detectando = False
    if enviar_temperatura and button_a.was_pressed():
        detectando = True
        while detectando:
            if button_a.was_pressed():
                # --- Botón A para enviar temperatura ---
                temp = temperature()  # función de micro:bit que devuelve temperatura en °C
                display.scroll(temp)
                values.append(temp)
                
            if button_b.was_pressed():
                detectando = False
                
        radio.on()
        radio.config(group=1, power=7)     
        radio.send(str(values))
        display.show(Image.TARGET)
        display.clear()
        enviar_temperatura = False  # solo enviamos una vez por presión