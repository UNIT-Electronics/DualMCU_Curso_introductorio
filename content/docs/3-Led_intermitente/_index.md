---
title: 3. Led intermitente (OUTPUT) 
type: docs
weight: 3
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 3. Led intermitente
### 3.1. Objetivo
Programar el microcontrolador para que parpadee un LED a una frecuencia específica. 



### 3.2. Descripción

Este apartado incluye dos códigos separados, uno para el ESP32 y otro para el RP2040. Cada archivo se puede correr bajo el nombre de **blink.py** que puedes cargar en la respectiva placa para hacer que un LED parpadee. A continuación,se te proporcionará un ejemplo simple de código MicroPython para el ESP32:

```python
'''
Unit Electronics 2023
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.1
   revision: 0.0.1

   context: This code provides a basic configuration for three RGB LEDs.
'''
import machine
import time

led_pin = machine.Pin(4, machine.Pin.OUT)
led_pin2 = machine.Pin(26, machine.Pin.OUT)
led_pin3 = machine.Pin(25, machine.Pin.OUT)


def loop():
     while True:
        led_pin.on()    
        led_pin2.on()   
        led_pin3.on()  
        time.sleep(1)  
        led_pin.off()   
        led_pin2.off()  
        led_pin3.off()  
        time.sleep(1)   

loop()
```
El código anterior sirve para testear la configuración de [instalación de Micropython en el ESP32](https://github.com/UNIT-Electronics/DualMCU-ESP32-MicroPython), en el cual se encienden los tres leds y se apagan en un intervalo de 1 segundo. 
Puedes modificar el código para que el led parpadee a una frecuencia diferente. Por ejemplo, si cambias el valor de la función `time.sleep(1)` a `time.sleep(0.5)`, el LED parpadeará cada 0.5 segundos.

En la siguiente imagen puedes ver el resultado de este código:

+ ![](/docs/3-Led_intermitente/images/blink_led2.gif)

Y aquí tienes un ejemplo similar para el RP2040:

```python
'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
context: This code is a basic configuration of a led
'''
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)  # Configura el pin GPIO25 como salida

while True:
    led.value(not led.value())  # Invierte el estado del LED (encendido/apagado)
    utime.sleep(1)  # Espera 1 segundo
```
Puedes personalizar estos ejemplos según tus necesidades y cargarlos en las respectivas placas. Asegúrate de seguir las instrucciones en el repositorio para configurar correctamente el entorno de desarrollo para MicroPython en cada placa antes de cargar el código.

También encontrarás un ejemplo de un código en el repositorio oficial: [blink.py](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/00.LEDs/blink.py)

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.
---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊