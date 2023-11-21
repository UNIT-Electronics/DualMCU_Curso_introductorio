    ---
title: 10. Control de pantalla OLED (I2C)
type: docs
weight: 10
BookToC: false
---

# Prácticas con la DualMCU

## 10. Control de pantalla OLED
### 10.1. Objetivo
El objetivo de este proyecto es programar el microcontrolador DualMCU para mostrar información en una pantalla OLED. 

- Mostrar la hora actual en formato de reloj digital.
- Crear un contador regresivo con la capacidad de configurar el tiempo deseado.
- Visualizar datos en tiempo real de sensores ambientales, como temperatura, humedad, calidad del aire, etc.



### 10.2 Requisitos
+ Microcontrolador DualMCU.
+ Pantalla  OLED compatible.
+ Sensores ambientales si se desea mostrar datos en tiempo real.
+ Conexiones eléctricas y fuente de alimentación adecuadas.


### 10.3. Descripción
Este apartado tiene como objetivo proporcionar una plataforma versátil para visualizar datos relevantes en un formato fácilmente comprensible y personalizable.



```python

from machine import Pin, I2C
import ssd1306
import time

# Inicializar I2C
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

# Inicializar la pantalla OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def get_current_time():
    # Implementar la función para obtener la hora actual
    pass

def create_countdown(seconds):
    # Implementar la función para crear un contador regresivo
    pass

def read_sensor_data():
    # Implementar la función para leer los datos de los sensores ambientales
    pass

while True:
    # Obtener la hora actual
    current_time = get_current_time()

    # Crear un contador regresivo
    countdown = create_countdown(10)  # 10 segundos para el ejemplo

    # Leer los datos de los sensores ambientales
    sensor_data = read_sensor_data()

    # Mostrar los datos en la pantalla OLED
    display.fill(0)
    display.text('Hora: ' + current_time, 0, 0)
    display.text('Contador: ' + countdown, 0, 10)
    display.text('Datos del sensor: ' + sensor_data, 0, 20)
    display.show()

    time.sleep(1)


```

    1. Inicializar el microcontrolador DualMCU.
    1. Inicializar la pantalla OLED.
    1. Crear una función para obtener la hora actual del sistema y formatearla en formato de reloj digital.
    1. Crear una función para un contador regresivo que acepte un tiempo de entrada.
    1. Inicializar los sensores ambientales.
    1. Crear una función para leer los datos de los sensores ambientales.
    1. Crear una función para mostrar los datos en la pantalla OLED.

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Ten en cuenta que este es solo un esquema y necesitarás implementar las funciones `getCurrentTime`, `createCountdown` y `readSensorData` según tus necesidades. También necesitarás incluir las librerías adecuadas para tu microcontrolador y sensores.