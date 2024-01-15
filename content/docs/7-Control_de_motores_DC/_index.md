---
title: 7. Control de motores DC
type: docs
weight: 7
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 7. Control de motores DC
### 7.1. Objetivo
Diseñar un sistema de control de motores de corriente continua (DC) con un microcontrolador. 


### 7.2. Descripción
Controlar la velocidad y dirección de los motores DC de manera precisa.

#### 7.2.1 Aplicación 
- Implementar un sistema de control que permita que el robot se mueva de manera autónoma o en respuesta a comandos externos.
- Conexión con interfaz de usuario para personalizar el comportamiento del robot.
- Flexibilidad para la expansión y personalización del sistema de control.

### 7.3 Requisitos
+ 1x Placa de desarrollo [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ Motores de corriente continua (DC).
+ Sensores y componentes adicionales según los requisitos del robot, te recomendamos dos alternativas:
    + [Kit Carrito 4WD Robot Educacional con Accesorios](https://uelectronics.com/producto/kit-carrito-4wd-robot-educacional-con-accesorios/)
    + [Kit Carrito Robot Seguidor Lineas Con Accesorios](https://uelectronics.com/producto/kit-carrito-robot-seguidor-lineas-con-accesorios/)
+ [L298N Módulo Driver Motor A pasos](https://uelectronics.com/producto/l298n-modulo-driver-motor-a-pasos/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.



Puedes controlar un motor de corriente continua (DC) con el controlador L298N sin usar PWM, pero  significa que el motor solo podrá estar encendido o apagado, y no se podrá controlar su velocidad.

En el siguiente bloque de código presento un  ejemplo de cómo usarlo en MicroPython para el RP2040:

```python
from machine import Pin

# Configura los pines para controlar el L298N
l298n_enable = Pin(4, Pin.OUT)  # Conecta a EN del L298N
l298n_input1 = Pin(12, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(13, Pin.OUT)  # Conecta a IN2 del L298N

# Habilita el motor
l298n_enable.on()

# Control del motor
l298n_input1.on()  # Motor en un sentido
l298n_input2.off()  # Motor en el otro sentido
```

Este código hará que el motor gire en un sentido a toda velocidad. Si quieres cambiar la dirección del motor, puedes intercambiar los estados de `l298n_input1` y `l298n_input2`.

El cambio si lo prefieres puedes controlar la velocidad con la que puedas moverte, el uso del PWM puedes ser una alternativa. 
```python

from machine import Pin, PWM

# Configura los pines para controlar el L298N
l298n_enable = Pin(4, Pin.OUT)  # Conecta a EN del L298N
l298n_input1 = PWM(Pin(12, Pin.OUT))  # Conecta a IN1 del L298N
l298n_input2 = PWM(Pin(13, Pin.OUT))  # Conecta a IN2 del L298N

# Habilita el motor
l298n_enable.on()

# Define la velocidad del motor (ajusta el valor según sea necesario)
motor_speed = 512

# Control del motor
l298n_input1.duty(motor_speed)  # Motor en un sentido
l298n_input2.duty(0)  # Motor en el otro sentido


```



### 5.5 Instrucciones de Uso

1. Importa las clases `Pin` y `PWM` del módulo `machine`.
2. Configura los pines GPIO para controlar el L298N. Los pines EN1 y EN2 del L298N se conectan a los pines GPIO 4 y 5 del ESP32, respectivamente. Los pines IN1, IN2, IN3 e IN4 del L298N se conectan a los pines GPIO 12, 13, 14 y 15 del ESP32, respectivamente.
3. Habilita los motores configurando los pines EN1 y EN2 en alto.
4. Define la velocidad de los motores ajustando el ciclo de trabajo de los pines PWM. En este caso, la velocidad del motor se establece en 512 (en una escala de 0 a 1023).
5. Controla los motores ajustando el ciclo de trabajo de los pines IN1, IN2, IN3 e IN4. Para hacer girar un motor en sentido horario, configura el ciclo de trabajo del pin correspondiente a la velocidad del motor y el otro pin a 0. Para hacer girar un motor en sentido antihorario, haz lo contrario.
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



[![Demo Video]](/docs/7-Control_de_motores_DC/images/vid1.mp4)

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.


---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊

