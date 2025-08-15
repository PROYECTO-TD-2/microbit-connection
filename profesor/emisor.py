from microbit import *
import radio

# Activamos el radio
radio.on()
# Configuramos un grupo para que solo ciertos micro:bits se comuniquen
radio.config(group=1)
message = ""

while True:
    # Verificamos si hay datos disponibles en el puerto serial
    if uart.any():
        # Leemos los datos del puerto serial
        serial_data = uart.readline()
        # Convertimos los datos a string y eliminamos caracteres de nueva línea
        if serial_data:
            message = serial_data.decode('utf-8').strip()
            
            # Enviamos el mensaje recibido por radio
            radio.send(message)
            
            # Mostramos una indicación visual de que se envió el mensaje
            display.show(Image.CHESSBOARD)
            sleep(500)
            display.clear()
            
            # Opcional: mostrar el mensaje enviado en la pantalla
            # display.scroll(message)
    
    # Pequeña pausa para no saturar el procesador
    sleep(100)