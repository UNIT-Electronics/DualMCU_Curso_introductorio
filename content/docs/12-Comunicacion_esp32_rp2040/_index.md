    ---
title: 12. Comunicación entre ESP32 y RP2040 
type: docs
weight: 10
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

##    12. Comunicación entre microcontrolador ESP32 y RP2040

### Objetivo
Establecer una comunicación efectiva entre dos microcontroladores de la DualMCU, con el fin de unificar recursos y potenciar el poder de procesamiento en aplicaciones que requieran mayores capacidades.

### Descripción 
Esta práctica proporciona una solución para lograr una comunicación eficiente entre dos microcontroladores, específicamente el ESP32 y el RP2040. La implementación está diseñada para optimizar el rendimiento en aplicaciones que demandan mayores recursos computacionales.

### Requisitos
- <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
- <a href="https://uelectronics.com/producto/cable-usb-tipo-c-3a-6a/" target="_blank">Cable USB Tipo C</a>


### Diagrama de Conexión
A continuación, se muestra el diagrama de conexión, el cual es muy sencillo: solo necesitas conectar la UNIT DUALMCU a tu laptop o computadora de escritorio mediante un cable USB Tipo C.


![pc](/docs/3-Led_intermitente/images/pc_dual.jpg)


Cambia el Interruptor DIP UART a "ON" para esta configuración.
       <div style="text-align: center;">
       <img src="/docs/12-Comunicacion_esp32_rp2040/images/SEL.png" alt="Block Diagram" title="Block Diagram" >
       </div>

Para esta práctica, necesitarás cambiar entre microcontroladores. Se te recuerda que a través del selector puedes intercambiar entre microcontroladores.
 Después de conectar la UNIT DUALMCU al ordenador, procede a encender el dispositivo y seleccionar el microcontrolador (MCU) deseado.
<div style="text-align: center;">
<img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
</div>

### Código 


El proceso se lleva a cabo en dos partes. La primera etapa implica la carga del código en el RP2040, lo cual debe realizarse de la siguiente manera: selecciona la placa en el COM en la parte inferior derecha.

<div style="text-align: center;">
<img src="/docs/12-Comunicacion_esp32_rp2040/images/RP2040_COM.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

Copia el siguiente código:

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

Guarda el código en el RP2040, seleccionando **Raspberry Pi Pico**.

<div style="text-align: center;">
<img src="/docs/12-Comunicacion_esp32_rp2040/images/SELECT_SAVE.png" alt="Block Diagram" title="Block Diagram" style="width: 200px;">
</div>


Te aparecerá una ventana en la que deberás escribir el nombre **main.py** y finalmente presionar ***ok***.
<div style="text-align: center;">

<img src="/docs/12-Comunicacion_esp32_rp2040/images/SAVE_MAIN.png" alt="Block Diagram" title="Block Diagram" style="width: 500px;">
</div>

Cierra tu ventana y cambia de microcontrolador con el selector USB al **ESP32**.
<div style="text-align: center;">
<img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
</div>
Conecta el ESP32 y selecciona el microcontrolador:
<div style="text-align: center;">
<img src="/docs/12-Comunicacion_esp32_rp2040/images/ESP32_COM.png" alt="Block Diagram" title="Block Diagram" style="width: 500px;">
</div>

Copia el siguiente código:

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
Corre el código del ESP32 debe aparecer el los datos enviados por el RP2040.


<div style="text-align: center;">
<img src="/docs/12-Comunicacion_esp32_rp2040/images/shell1.png" alt="Block Diagram" title="Block Diagram" >
</div>

### Resultados

Con unos breves resultados, el control de comunicación por JSON es una práctica que beneficia la comunicación en el aspecto de que los microcontroladores permiten su uso sin componentes de software externos, por lo que su implementación es práctica. Los resultados de esta comunicación permiten conocer las posibilidades de la DUALMCU. 
<div style="text-align: center;">
<img src="/docs/12-Comunicacion_esp32_rp2040/images/dual.gif" alt="Block Diagram" title="Block Diagram" >
</div>

### Conclusiones

En conclusión, el objetivo de la práctica es lograr una comunicación efectiva entre dos microcontroladores de la DualMCU, el ESP32 y el RP2040, con el propósito de consolidar recursos y potenciar el poder de procesamiento. La implementación busca ofrecer una solución que optimice el rendimiento en aplicaciones que requieren mayores capacidades computacionales, brindando así una solución eficiente para proyectos que demandan un mayor nivel de procesamiento y coordinación entre microcontroladores.


###  DualMCU ESP32+RP2040 

Para obtener más información, consulte las páginas del producto en

* https://uelectronics.com/
* [Hardware-DualMCU](https://github.com/UNIT-Electronics/DualMCU/tree/main/Hardware)
* [Product Reference Manual.pdf](https://github.com/UNIT-Electronics/DualMCU/blob/main/DualMCU(Product%20Reference%20Manual).pdf)
* [C++ & Micropython Examples files for the UNIT DualMCU.](https://github.com/UNIT-Electronics/DualMCU/tree/main/Examples)
* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊
 
