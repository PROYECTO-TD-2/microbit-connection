from microbit import *
import radio

# Encender radio y configurar grupo
radio.on()
radio.config(group=1)

# Inicializar UART
uart.init(baudrate=115200)

while True:
    # --- UART → RADIO --- UART (Universal Asynchronous Receiver/Transmitter)
    if uart.any():
        serial_data = uart.readline()
        if serial_data:
            message = serial_data.decode('utf-8').strip()
            
            # Enviar al alumno por radio
            radio.send(message)
            
            # Feedback visual
            display.show(Image.CHESSBOARD)
            sleep(300)
            display.clear()
            
            # Confirmación por UART
            uart.write("Mensaje enviado: " + message + "\n")
    
    # --- RADIO → UART ---
    msg = radio.receive()
    if msg:
        # Mostrar feedback visual
        display.show(Image.YES)
        sleep(300)
        display.clear()

        # Reenviar al navegador
        uart.write("Respuesta alumno: " + msg + "\n")
    
    sleep(100)
