---
title: 3. Led intermitente
type: docs
weight: 3
BookToC: false
---

# Prácticas con la DualMCU

## 3. Led intermitente
### 3.1. Objetivo
Programar el microcontrolador para que parpadee un LED a una frecuencia
específica. 

Esto es una introducción básica a la programación de microcontroladores y permitirá
aprender sobre la configuración de pines y temporizadores.

### 3.2. Descripción

Este apartado incluye dos códigos separados, uno para el ESP32 y otro para el RP2040.Cada archivo se puede correr bajo el nombre de led_intermitente.py que puedes cargar en la respectiva placa para hacer que un LED parpadee. A continuación, te proporcionaré un ejemplo simple de código MicroPython para el ESP32:

```python
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Configura el pin GPIO2 como salida

while True:
    led.value(not led.value())  # Invierte el estado del LED (encendido/apagado)
    time.sleep(1)  # Espera 1 segundo
```
Y aquí tienes un ejemplo similar para el RP2040:

```python

import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)  # Configura el pin GPIO25 como salida

while True:
    led.value(not led.value())  # Invierte el estado del LED (encendido/apagado)
    utime.sleep(1)  # Espera 1 segundo
```
Puedes personalizar estos ejemplos según tus necesidades y cargarlos en las respectivas placas. Asegúrate de seguir las instrucciones en el repositorio para configurar correctamente el entorno de desarrollo para MicroPython en cada placa antes de cargar el código.