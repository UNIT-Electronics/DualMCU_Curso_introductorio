---
title: 5.  Control Servo (PWM)
type: docs
weight: 5
BookToC: false
---

# Prácticas con la DualMCU

## 5. Control Servo
### 5.1. Objetivo
Utiliza el microcontrolador de tu preferencia para controlar un servo motor y hacer que gire a
ángulos específicos. Se puede hacer que el servo se mueva a través de un rango de ángulos
determinado o que siga una secuencia predefinida.

### 5.2. Descripción

Este apartado contiene un conjunto de recursos y código para controlar un servomotor utilizando MicroPython. Los servomotores son dispositivos ampliamente utilizados en proyectos de robótica y automatización para controlar la posición angular de un eje. Con MicroPython, puedes controlar un servomotor de manera sencilla y eficaz.

### 5.3 Requisitos
+ 1x [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ 1x [Servomotor compatible](https://uelectronics.com/producto/servomotor-sg90-rc-9g/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.

### 5.4 Contenido del Repositorio
**Código Fuente:** Este repositorio incluye el código fuente necesario para controlar un servomotor con MicroPython. 

Para controlar la velocidad de un servomotor con un microcontrolador ESP32, puedes ajustar el ancho del pulso de la señal PWM que envías al servomotor. Aquí tienes un ejemplo de cómo hacerlo en MicroPython:

```python
from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(15), freq=50)  # Configura el pin GPIO 15 como salida PWM con una frecuencia de 50Hz

def set_angle(angle):
    duty = angle / 180 * 1023
    servo.duty(int(duty))

def move_servo_slowly_to(angle):
    current_angle = 0
    while current_angle < angle:
        set_angle(current_angle)
        sleep(0.01)  # Ajusta este valor para controlar la velocidad del movimiento del servo
        current_angle += 1

move_servo_slowly_to(90)  # Mueve el servo lentamente a 90 grados
```

Este código define una función `move_servo_slowly_to(angle)` que mueve el servomotor a un ángulo especificado a una velocidad controlada por el tiempo de espera en el bucle while. Puedes ajustar el valor de sleep para controlar la velocidad del servomotor.

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Con el fin de mejorar tu habilidad puedes checar el ejemplo relacionadon con el pwm del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/02.PWM/PWM.py)




