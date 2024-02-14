'''
rp2040

'''

import time
from machine import UART, Pin
import ujson

uart1 = UART(0, baudrate=115000, tx=Pin(0, Pin.OUT), rx=Pin(1, Pin.IN))

led_sequence = ["rojo", "verde", "azul"]  # Lista que define la secuencia de LEDs

while True:
    time.sleep(0.1)

    # Obtén el siguiente LED en la secuencia
    led_actual = led_sequence.pop(0)
    
    # Añade el estado del LED actual al JSON
    datos = {
        "led_actual": led_actual,
        "accion": "encender"
    }
    txData = ujson.dumps(datos)
    uart1.write(txData + '\n\r')
    print(txData)

    time.sleep(1)  # Espera 1 segundo antes de enviar el siguiente conjunto de datos

    # Añade el estado del LED actual al JSON
    datos = {
        "led_actual": led_actual,
        "accion": "apagar"
    }
    txData = ujson.dumps(datos)
    uart1.write(txData + '\n\r')
    print(txData)

    # Mueve el LED actual al final de la secuencia
    led_sequence.append(led_actual)

    time.sleep(1)  # Espera 1 segundo antes de enviar el siguiente conjunto de datos
