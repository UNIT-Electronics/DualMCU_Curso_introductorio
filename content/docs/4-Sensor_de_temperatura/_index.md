---
title: 4. Sensor de termperatura
type: docs
weight: 4
BookToC: false
---

# Prácticas con la DualMCU

## 4. Sensor de temperatura
### 4.1. Objetivo
Conectar un sensor de temperatura (como el LM35) al microcontrolador y
programar para que muestre la temperatura actual en un display LCD o en un monitor serie. Esto te
ayudará a trabajar con sensores analógicos y a interpretar datos de sensores.

### 4.2. Descripción

Este apartado incluye dos códigos separados, uno para el ESP32 y otro para el RP2040. Cada archivo se puede correr bajo el nombre de sensor.py que puedes cargar en la respectiva placa para hacer que un LED parpadee. A continuación, te proporcionaré un ejemplo simple de código MicroPython para el ESP32:

```python

import machine
import time
# configura entrada de adc en el pin 36
adc = machine.ADC(machine.Pin(36))
# configura el rango de lectura de 0 a 3.3v
adc.atten(machine.ADC.ATTN_11DB)
# configura el rango de lectura de 0 a 4095
adc.width(machine.ADC.WIDTH_12BIT)
# configura el pin 2 como salida
led = machine.Pin(2, machine.Pin.OUT)
# configura el pin 25 como salida
led2 = machine.Pin(25, machine.Pin.OUT)

#Comienza el ciclo infinito

while True:
    #lee el valor del adc
    valor = adc.read()
    #imprime el valor del adc
    print(valor)
    #si el valor es mayor a 2000 enciende el led
    if valor > 2000:
        led.value(1)
        led2.value(0)
    #si el valor es menor a 2000 enciende el led
    else:
        led.value(0)
        led2.value(1)               
    #espera 1 segundo       
    time.sleep(1)

```
