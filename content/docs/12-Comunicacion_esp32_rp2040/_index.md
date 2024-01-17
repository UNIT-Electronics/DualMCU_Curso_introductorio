    ---
title: 12. Comunicación entre ESP32 y RP2040 
type: docs
weight: 10
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

##    12. Comunicación entre microcontrolador ESP32 y RP2040

## Objetivo
Establecer una comunicación efectiva entre dos microcontroladores de la DualMCU, con el fin de unificar recursos y potenciar el poder de procesamiento en aplicaciones que requieran mayores capacidades.

## Descripción 
Esta práctica proporciona una solución para lograr una comunicación eficiente entre dos microcontroladores, específicamente el ESP32 y el RP2040. La implementación está diseñada para optimizar el rendimiento en aplicaciones que demandan mayores recursos computacionales.

## Requisitos
- Placa de desarrollo DualMCU con microcontroladores ESP32 y RP2040.
- Entorno de desarrollo integrado (IDE) compatible con ambos microcontroladores.

## Diagrama de Conexión

Para esta practica necesitaras estar cambiando entre microcontroladores se te recuerda que atraves del selector puedes intercambiar entre mirocontroladores.

## Código 
El código fuente se encuentra en el directorio. A continuación, se proporciona un ejemplo básico de cómo establecer la comunicación entre los microcontroladores:


Conecta el RP2040

```py
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


```

Cierra tu ventana y cambia de microcontrolador con el selector USB

Conecta el ESP32


```py
'''
ESP32
'''
import ujson
from machine import UART, Pin

uart0 = UART(1, baudrate=115000, tx=Pin(17, Pin.OUT), rx=Pin(16, Pin.IN))
led_rojo = Pin(4, Pin.OUT)  # Configura el pin GPIO5 como salida para el LED rojo
led_verde = Pin(26, Pin.OUT)  # Configura el pin GPIO18 como salida para el LED verde
led_azul = Pin(25, Pin.OUT)  # Configura el pin GPIO19 como salida para el LED azul

def ejecutar_accion(accion, pin_led):
    if accion == "encender":
        pin_led.on()  # Enciende el LED
    elif accion == "apagar":
        pin_led.off()  # Apaga el LED

def recibir_json():
    rx_data = b''  # Inicializa una cadena de bytes vacía

    while True:
        if uart0.any():
            byte_received = uart0.read(1)  # Lee un byte desde el UART
            rx_data += byte_received

            # Verifica si el carácter de nueva línea indica el final del JSON
            if byte_received == b'\n':
                try:
                    # Intenta cargar el JSON
                    json_data = ujson.loads(rx_data.decode('utf-8'))
                    print("JSON recibido:", json_data)
                    
                    # Extrae los valores de 'accion' y 'led_actual' del JSON
                    accion = json_data.get('accion', '')
                    led_actual = json_data.get('led_actual', '')

                    # Ejecuta la acción indicada en el JSON para cada LED
                    if led_actual == "rojo":
                        ejecutar_accion(accion, led_rojo)
                    elif led_actual == "verde":
                        ejecutar_accion(accion, led_verde)
                    elif led_actual == "azul":
                        ejecutar_accion(accion, led_azul)
                    print("--led recibido:", led_actual, "accion:", accion)
                    
                    return json_data
                except ValueError as e:
                    print("Error al parsear JSON:", e)
                    rx_data = b''  # Reinicia la cadena si hay un error en el JSON

# Ejemplo de uso
while True:
    data = recibir_json()
    # Realiza acciones con el JSON recibido

```




###  DualMCU ESP32+RP2040 

Para obtener más información, consulte las páginas del producto en

* https://uelectronics.com/
* [Hardware-DualMCU](https://github.com/UNIT-Electronics/DualMCU/tree/main/Hardware)
* [Product Reference Manual.pdf](https://github.com/UNIT-Electronics/DualMCU/blob/main/DualMCU(Product%20Reference%20Manual).pdf)
* [C++ & Micropython Examples files for the UNIT DualMCU.](https://github.com/UNIT-Electronics/DualMCU/tree/main/Examples)
* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊
 
