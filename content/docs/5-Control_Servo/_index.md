---
title: 5.  Control Servo (PWM)
type: docs
weight: 5
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 5. Control Servo
### 5.1. Objetivo
Utilizar la tarjeta DualMCU con el RP2040 para controlar un servo motor, logrando movimientos precisos a ángulos específicos. Esto incluye la capacidad de dirigir el servo en un rango definido o seguir una secuencia predefinida de movimientos.

### 5.2. Descripción

Esta sección proporciona un conjunto de recursos y código diseñado para el control de servomotores mediante MicroPython. Los servomotores, comúnmente empleados en proyectos de robótica y automatización, permiten la gestión precisa de la posición angular de un eje. A través de MicroPython, se facilita una interfaz sencilla y eficiente para el control efectivo de servomotores, brindando a los usuarios la capacidad de incorporar este componente de manera fácil y efectiva en sus proyectos.

### 5.3 Requisitos
+ 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>

+ 1x <a href="https://uelectronics.com/producto/servomotor-sg90-rc-9g/" target="_blank">Servomotor compatible</a>


+ 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>

### 5.4 Diagrama de conexión

<div style="text-align: center;">
    <img src="/docs/5-Control_Servo/images/Diagrama.jpg" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

### 5.5 Código Fuente:

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

```py
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

![](/docs/5-Control_Servo/images/pwm_servo.gif)

### 5.6 Resultados

Los resultados obtenidos del código implementado con MicroPython en el RP2040 demuestran un eficiente control del servomotor mediante modulación por ancho de pulso (PWM). En el código, el pin GPIO 0 (ajustable según las conexiones) se configura como un canal PWM, y se establece una frecuencia de 50 Hz, comúnmente utilizada para el control de servomotores.

La función set_servo_angle(angle) convierte los ángulos deseados (de 0 a 180 grados) en valores de ciclo de trabajo específicos para el servomotor. Dentro de un bucle infinito, el código logra un movimiento suave del servomotor de 0 a 180 grados y viceversa, con pausas breves entre cada posición. Es posible interrumpir el programa con Ctrl+C, deteniendo el PWM y liberando los recursos.

Este código proporciona una base sólida para el control de servomotores con el RP2040 y es fácilmente adaptable a las especificaciones particulares de cualquier servomotor. La capacidad de ajustar la configuración, frecuencia y ángulos hace que este código sea versátil y aplicable a una variedad de proyectos que requieran control preciso de servomotores.

El código proporcionado utiliza MicroPython en el RP2040 para controlar un servomotor mediante modulación por ancho de pulso (PWM). El pin GPIO 0 (puede ajustarse según las conexiones) se configura como un canal PWM, y se establece una frecuencia de 50 Hz para el PWM, un valor comúnmente utilizado para servomotores. La función set_servo_angle(angle) convierte los ángulos deseados (de 0 a 180 grados) en valores de ciclo de trabajo específicos para el servomotor. Luego, en un bucle infinito, el código mueve suavemente el servomotor de 0 a 180 grados y viceversa, con pausas breves entre cada posición. El programa se puede interrumpir con Ctrl+C, lo que detendrá el PWM y liberará los recursos. Este código sirve como punto de partida para controlar servomotores con el RP2040 y se puede adaptar según las especificaciones de tu servomotor.


### 5.7 Conclusiones 
La práctica con la tarjeta DualMCU - RP2040 y un servomotor brinda una introducción valiosa al control de dispositivos físicos mediante microcontroladores. La capacidad demostrada por el RP2040 para gestionar las señales de control del servomotor ofrece una comprensión práctica de los pines GPIO y la generación de pulsos PWM para dirigir la posición y el movimiento del motor.

Esta experiencia sienta una base sólida para abordar aplicaciones más complejas en el control de dispositivos, ya sea en proyectos de robótica, automatización o sistemas embebidos. El conocimiento adquirido durante esta práctica proporciona una plataforma para explorar y desarrollar soluciones más avanzadas, permitiendo a los usuarios mejorar sus habilidades en el ámbito del control de hardware mediante microcontroladores.

Para continuar mejorando en estas habilidades, se recomienda revisar y experimentar con ejemplos relacionados con PWM en el repositorio de la DualMCU, lo que permitirá una comprensión más profunda y aplicada de los conceptos aprendidos durante esta práctica.


> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Con el fin de mejorar tu habilidad puedes checar el ejemplo relacionadon con el pwm del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/02.PWM/PWM.py)


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊


