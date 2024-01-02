---
title: 5.  Control Servo (PWM)
type: docs
weight: 5
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

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

```python 
'''
Unit Electronics 2023
          (o_
   (o_    //\
   (/)_   V_/_ 
tested code mark
   version: 0.0.1
   revision: 0.0.1

Código de prueba
'''
import machine
import utime

# Configuración del pin PWM
pwm_pin = machine.Pin(0)  # Cambia a machine.Pin(1) si estás usando el pin GPIO 1
pwm = machine.PWM(pwm_pin)

# Frecuencia del PWM en Hz (ajusta según tus necesidades)
pwm.freq(1000)

try:
    while True:
        # Ciclo de trabajo del PWM (0-65535, donde 0 es apagado y 65535 es encendido)
        for duty_cycle in range(0, 65536, 5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

        # Invierte el ciclo de trabajo para un efecto de atenuación
        for duty_cycle in range(65535, -1, -5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

except KeyboardInterrupt:
    # Detén el PWM y limpia los recursos al interrumpir el programa con Ctrl+C
    pwm.deinit()
    print("\nPWM detenido. Recursos liberados.")




```

![](/docs/5-Control_Servo/images/pwm_osc.gif)

Para controlar la velocidad de un servomotor con un microcontrolador ESP32, puedes ajustar el ancho del pulso de la señal PWM que envías al servomotor. Aquí tienes un ejemplo de cómo hacerlo en MicroPython:

```python
import machine
import utime

# Configuración del pin de control del servomotor (puedes cambiarlo según tus conexiones)
servo_pin = machine.Pin(0)  # Cambia a tu pin deseado

# Crea un objeto PWM para controlar el servomotor
pwm_servo = machine.PWM(servo_pin)

# Frecuencia del PWM para el servomotor (generalmente alrededor de 50 Hz)
pwm_servo.freq(50)

def set_servo_angle(angle):
    # Convierte el ángulo deseado (en grados) a un valor de ciclo de trabajo
    # Ten en cuenta que los valores específicos pueden variar según el servo
    duty_cycle = int(1024 + (angle / 180) * 3072)
    pwm_servo.duty_u16(duty_cycle)

try:
    while True:
        # Mueve el servomotor de 0 a 180 grados
        for angle in range(0, 181, 10):
            set_servo_angle(angle)
            utime.sleep(0.1)

        # Mueve el servomotor de 180 a 0 grados
        for angle in range(180, -1, -10):
            set_servo_angle(angle)
            utime.sleep(0.1)

except KeyboardInterrupt:
    # Detén el PWM y limpia los recursos al interrumpir el programa con Ctrl+C
    pwm_servo.deinit()
    print("\nPWM detenido. Recursos liberados.")

```
![](/docs/5-Control_Servo/images/pwm_osc.gif)

El código proporcionado utiliza MicroPython en el RP2040 para controlar un servomotor mediante modulación por ancho de pulso (PWM). El pin GPIO 0 (puede ajustarse según las conexiones) se configura como un canal PWM, y se establece una frecuencia de 50 Hz para el PWM, un valor comúnmente utilizado para servomotores. La función set_servo_angle(angle) convierte los ángulos deseados (de 0 a 180 grados) en valores de ciclo de trabajo específicos para el servomotor. Luego, en un bucle infinito, el código mueve suavemente el servomotor de 0 a 180 grados y viceversa, con pausas breves entre cada posición. El programa se puede interrumpir con Ctrl+C, lo que detendrá el PWM y liberará los recursos. Este código sirve como punto de partida para controlar servomotores con el RP2040 y se puede adaptar según las especificaciones de tu servomotor.

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Con el fin de mejorar tu habilidad puedes checar el ejemplo relacionadon con el pwm del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/02.PWM/PWM.py)


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊


