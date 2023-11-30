---
title: 9. Sistema de monitoreo ambiental
type: docs
weight: 9
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 9. Sistema de monitoreo ambiental 
### 9.1. Objetivo
Utiliza sensores para medir parámetros ambientales como temperatura, humedad, calidad del aire, etc. 
### 9.2. Descripción
Este apartado contiene un conjunto de recursos y código para construir un sistema de control ambiental utilizando un dispositivo ESP32 o RP2040 con MicroPython. Los sistemas de control ambiental son fundamentales para medir y gestionar parámetros como la temperatura, humedad, calidad del aire y otros factores para crear entornos cómodos y seguros.

### 9.5 Requisitos
+  1x Placa de desarrollo [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ Sensores de temperatura, humedad, calidad del aire, u otros sensores ambientales según tus necesidades.
+ Conexiones eléctricas y fuente de alimentación adecuadas.


### 9.3 Contenido del Repositorio
En este repositorio, encontrarás el código fuente necesario para monitorear y controlar parámetros ambientales. Se proporcionarán ejemplos de código que demuestran cómo utilizar sensores para medir temperatura, humedad, calidad del aire y otros factores.

Ejemplo de cómo podrías leer datos de un sensor de temperatura y humedad [DHT11](https://uelectronics.com/producto/modulo-ky-015-sensor-de-temperatura-y-humedad/) y un sensor de calidad del aire [MQ135](https://uelectronics.com/producto/mq-135-modulo-detector-de-calidad-de-aire/) con un ESP32 en MicroPython:

```python
from machine import Pin
import dht
import time
import adc

# Configura el sensor DHT11
dht_sensor = dht.DHT11(Pin(4))

# Configura el sensor MQ135
mq135_sensor = adc.ADC(Pin(36))

while True:
    # Lee la temperatura y la humedad del sensor DHT11
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    # Lee la calidad del aire del sensor MQ135
    air_quality = mq135_sensor.read()

    # Imprime los valores leídos
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %humidity)
    print('Air Quality: %d' %air_quality)

    # Espera un minuto antes de la próxima lectura
    time.sleep(60)
```

Este código lee la temperatura y la humedad del sensor DHT11 y la calidad del aire del sensor MQ135 cada minuto, e imprime los valores leídos.


> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Por ejemplo, podrías querer enviar los datos leídos a un servidor o a una base de datos en lugar de simplemente imprimirlos. Además, el sensor MQ135 necesita ser calibrado para proporcionar lecturas precisas de la calidad del aire.


