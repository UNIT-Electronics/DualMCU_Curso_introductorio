---
title: 5. Control Servo
type: docs
weight: 5
BookToC: false
---

# Prácticas con la DualMCU

## 5. Control Servo
### 5.1. Objetivo
Utilizar el microcontrolador para controlar un servo motor y hacer que gire a
ángulos específicos. Se puede hacer que el servo se mueva a través de un rango de ángulos
determinado o que siga una secuencia predefinida

### 5.2. Descripción

Este apartado contiene un conjunto de recursos y código para controlar un servomotor utilizando MicroPython. Los servomotores son dispositivos ampliamente utilizados en proyectos de robótica y automatización para controlar la posición angular de un eje. Con MicroPython, puedes controlar un servomotor de manera sencilla y eficaz.

### 5.3 Requisitos
+ 1x [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ 1x [Servomotor compatible](https://uelectronics.com/producto/servomotor-sg90-rc-9g/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.

### 5.4 Contenido del Repositorio
**Código Fuente:** Este repositorio incluye el código fuente necesario para controlar un servomotor con MicroPython. 

```python
'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
context: This code is a basic configuration of a servo motor
'''
import machine
from time import sleep

# Configura los pines PWM para los servos
pin1 = machine.Pin(15, machine.Pin.OUT)
pwm1 = machine.PWM(pin1)

# Configura las frecuencias y el rango del servo
pwm1.freq(50)

min_range = 4000  # Rango mínimo 
max_range = 8000  # Rango máximo 


transition_time = 0.5  
for _ in range(10):
    for duty in range(min_range, max_range):
        pwm1.duty_u16(duty)
        sleep(transition_time / (max_range - min_range))

    sleep(0.5)

    for duty in range(max_range, min_range, -1):
        pwm1.duty_u16(duty)
        sleep(transition_time / (max_range - min_range))

    sleep(0.5)

pwm1.deinit()


```

Con el fin de mejorar tu habilidad puedes checar el ejemplo relacionadon con el pwm del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/02.PWM/PWM.py)


**Diagramas de Conexión:** Se proporcionarán diagramas de conexión que muestran cómo conectar el servomotor a una placa de desarrollo compatible con MicroPython, como un dispositivo ESP32 o ESP8266.

**Instrucciones de Uso:** Se incluirán instrucciones detalladas sobre cómo cargar y ejecutar el código en tu placa de desarrollo. También se explicará cómo ajustar los parámetros para controlar el servomotor según tus necesidades específicas.

**Recursos Adicionales:** En este repositorio, se podrán incluir recursos adicionales, como enlaces a tutoriales y documentación relevante para comprender mejor el funcionamiento de los servomotores y MicroPython.

### 5.5 Instrucciones de Uso
1. Clona o descarga este repositorio a tu entorno de desarrollo de MicroPython.

1. Sigue las instrucciones de conexión proporcionadas en los diagramas de conexión.

1. Abre el código fuente en tu entorno de desarrollo MicroPython y carga el código en tu placa de desarrollo.

1. Ejecuta el código en tu placa de desarrollo y observa cómo se controla el servomotor.


