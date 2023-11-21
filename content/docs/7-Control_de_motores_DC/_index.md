---
title: 7. Control de motores DC
type: docs
weight: 7
BookToC: false
---

# Prácticas con la DualMCU

## 7. Control de motores DC
### 7.1. Objetivo
Diseñar un sistema de control de motores de corriente continua (DC) con un microcontrolador. Se puede programar un robot pequeño.


### 7.2. Descripción
Controlar la velocidad y dirección de los motores DC de manera precisa.
Implementar un sistema de control que permita que el robot se mueva de manera autónoma o en respuesta a comandos externos.
Proporcionar una interfaz de usuario para personalizar el comportamiento del robot.
Ofrecer flexibilidad para la expansión y personalización del sistema de control.

### 7.3 Requisitos
+ 1x Placa de desarrollo [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ Motores de corriente continua (DC).
+ Sensores y componentes adicionales según los requisitos del robot, te recomendamos dos alternativas:
    + [Kit Carrito 4WD Robot Educacional con Accesorios](https://uelectronics.com/producto/kit-carrito-4wd-robot-educacional-con-accesorios/)
    + [Kit Carrito Robot Seguidor Lineas Con Accesorios](https://uelectronics.com/producto/kit-carrito-robot-seguidor-lineas-con-accesorios/)
+ [L298N Módulo Driver Motor A pasos](https://uelectronics.com/producto/l298n-modulo-driver-motor-a-pasos/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.

Contenido del Repositorio

+ **Código Fuente:** El repositorio incluirá el código necesario para programar el microcontrolador y controlar los motores DC.

```python

from machine import Pin, PWM

# Configura los pines para controlar el LD298
ld298_enable1 = Pin(4, Pin.OUT)  # Conecta a EN1 del LD298
ld298_enable2 = Pin(5, Pin.OUT)  # Conecta a EN2 del LD298
ld298_input1 = PWM(Pin(12, Pin.OUT))  # Conecta a IN1 del LD298
ld298_input2 = PWM(Pin(13, Pin.OUT))  # Conecta a IN2 del LD298
ld298_input3 = PWM(Pin(14, Pin.OUT))  # Conecta a IN3 del LD298
ld298_input4 = PWM(Pin(15, Pin.OUT))  # Conecta a IN4 del LD298

# Habilita los motores
ld298_enable1.on()
ld298_enable2.on()

# Define la velocidad de los motores (ajusta el valor según sea necesario)
motor_speed = 512

ld298_input1.duty(motor_speed)  # Motor 1 en sentido horario
ld298_input2.duty(0)  # Motor 1 en sentido antihorario
ld298_input3.duty(motor_speed)  # Motor 2 en sentido horario
ld298_input4.duty(0)  # Motor 2 en sentido antihorario


```

```python
from machine import Pin, PWM

# Configura los pines para controlar el LD298
ld298_enable1 = Pin(4, Pin.OUT)  # Conecta a EN1 del LD298
ld298_enable2 = Pin(5, Pin.OUT)  # Conecta a EN2 del LD298
ld298_input1 = PWM(Pin(12, Pin.OUT))  # Conecta a IN1 del LD298
ld298_input2 = PWM(Pin(13, Pin.OUT))  # Conecta a IN2 del LD298
ld298_input3 = PWM(Pin(14, Pin.OUT))  # Conecta a IN3 del LD298
ld298_input4 = PWM(Pin(15, Pin.OUT))  # Conecta a IN4 del LD298

# Habilita los motores
ld298_enable1.on()
ld298_enable2.on()

# Define la velocidad de los motores (ajusta el valor según sea necesario)
motor_speed = 512

# Control de los motores
ld298_input1.duty(motor_speed)  # Motor 1 en sentido horario
ld298_input2.duty(0)  # Motor 1 en sentido antihorario
ld298_input3.duty(motor_speed)  # Motor 2 en sentido horario
ld298_input4.duty(0)  # Motor 2 en sentido antihorario

# Para controlar otros dos motores, configura los pines y la velocidad de manera similar.
# Por ejemplo:
# ld298_input5 = PWM(Pin(16, Pin.OUT))  # Conecta a IN1 del segundo LD298
# ld298_input6 = PWM(Pin(17, Pin.OUT))  # Conecta a IN2 del segundo LD298
# ld298_input7 = PWM(Pin(18, Pin.OUT))  # Conecta a IN3 del segundo LD298
# ld298_input8 = PWM(Pin(19, Pin.OUT))  # Conecta a IN4 del segundo LD298

# Habilita los motores
# ld298_enable3 = Pin(6, Pin.OUT)  # Conecta a EN1 del segundo LD298
# ld298_enable4 = Pin(7, Pin.OUT)  # Conecta a EN2 del segundo LD298
# ld298_enable3.on()
# ld298_enable4.on()

# Define la velocidad de los otros dos motores
# motor_speed2 = 768
# ld298_input5.duty(motor_speed2)
# ld298_input6.duty(0)
# ld298_input7.duty(motor_speed2)
# ld298_input8.duty(0)

```





+ **Recursos Adicionales:** Se pueden incluir enlaces a recursos adicionales, como tutoriales sobre el uso de sensores, programación de movimientos autónomos y consejos para la mejora del rendimiento del robot.




