---
title: 7. Control de motores DC
type: docs
weight: 7
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 7. Control de motores DC
###  Objetivo
Se realizará un sistema de control de motores de corriente directa (DC) con ayuda de un driver L298N.
>**NOTA** En esta práctica, se utilizará el **RP2040**.


###  Descripción
Los sistemas de control son parte integral de nuestra sociedad actual, tienen múltiples aplicaciones, desde mantener una temperatura deseada hasta mantener la estación espacial en órbita. 

La definición para sistema de control es: conjunto de procesos que en conjunto nos ayudan a obtener una salida esperada con un desempeño deseado dada una entrada específica. 

Un sistema de control de motores DC puede ser fácilmente adecuado para diferentes aplicaciones como las que se mencionan a continuación:

   - Propulsión de vehículos
   - Robots Móviles
      - Drones
      - Robots con ruedas u orugas
   - Sistemas de refrigeración
      - Control de ventiladores
      - Extracción de humos
   - Instalaciones de transporte
      - Bandas de transporte
   - Sistemas de automatización
      - Persianas/Cortinas inteligentes
   - Electrodomésticos y herramientas
      - Aspiradoras
      - Licuadoras
      - Dremel
      - Esmeril 
      - Taladros

Si bien, existe una mayor cantidad, se da una amplia idea de las aplicaciones que existen para los motores DC. 

Esta práctica se enfocará en realizar un sistema para controlar la velocidad y dirección de motores DC de manera precisa utilizando un dispositivo ESP32 o RP2040 con MicroPython. 




### Requisitos
- 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
- 2x <a href="https://uelectronics.com/producto/l298n-modulo-driver-motor-a-pasos/" target="_blank">Motores de corriente continua (DC).</a>
- 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Driver L298N</a>
- 1x <a href="https://uelectronics.com/producto/cable-de-alambre-estanado-24awg-25cm-100-piezas/" target="_blank">Alambre 24 AWG</a>
- 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>
- Alimentación de 12 V

+ Opcionalmente te recomendamos los kits de robótica que cuentan con motores y drivers:
- 1x <a href="https://uelectronics.com/producto/kit-carrito-4wd-robot-educacional-con-accesorios/" target="_blank">Kit Carrito 4WD Robot Educacional con Accesorio</a>
- 1x <a href="https://uelectronics.com/producto/kit-carrito-robot-seguidor-lineas-con-accesorios/" target="_blank">Kit Carrito Robot Seguidor Lineas Con Accesorioso</a>

### 7.4 Diagramas de Conexión
Diagrama para controlar un motor
<div style="text-align: center;">
<img src="/docs/7-Control_de_motores_DC/images/UnMotor_bb.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

Diagrama para controlar dos motores
<div style="text-align: center;">
<img src="/docs/7-Control_de_motores_DC/images/DosMotores_bb.png" alt="Block Diagram" title="Block Diagram" style="width: 700px;">
</div>



###  Código
Una vez realizadas las conexiones para un motor puedes controlar dicho motor de corriente continua (DC) con el controlador L298N sin usar PWM con ayuda del siguiente código. Ten en cuenta que el motor solo podrá estar encendido o apagado, y no se podrá controlar su velocidad.

> **NOTA:** Código realizado para MicroPython utilizando la DualMCU con el microprocesador RP2040. Recuerda que tu puedes intercambiar entre microcontroladores con  el selector USB.
>       
<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
    </div>

<div style="text-align: right;">
    <a href="/docs/7-Control_de_motores_DC/code/unitRP2040_motors1.py" download="unitRP2040_motors1.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitRP2040_motors1.py
        </button>
    </a>
</div>

```python
from machine import Pin
import time

# Configura los pines para controlar el L298N
l298n_enable = Pin(7, Pin.OUT)  # Conecta a EN del L298N
l298n_input1 = Pin(14, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(9, Pin.OUT)  # Conecta a IN2 del L298N

# Habilita el motor
l298n_enable.on()
# Control del motor
l298n_input1.on()
l298n_input2.off()

#Espera 5s
time.sleep(5)
#Deshabilita el motor
l298n_enable.off()

#Espera 1s
time.sleep(1)
#Habilita el motor
l298n_enable.on()
# Control del motor, sentido contrario
l298n_input1.off()  
l298n_input2.on()  

#Espera 5s
time.sleep(5)
l298n_enable.off()


```
El siguiente paso es controlar la velocidad del motor, tendrás que hacer uso de PWM para este fin. La velocidad máxima del motor la logras con el valor 65536, te recomendamos hacer pruebas con diferentes valores para encontrar las velocidades adecuadas a tus proyectos. 
####  Comprobar los valores de PWM para diferentes velocidades, empezando con el valor mínimo y máximo.

<div style="text-align: right;">
    <a href="/docs/7-Control_de_motores_DC/code/unitRP2040_motors2.py" download="unitRP2040_motors2.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitRP2040_motors2.py
        </button>
    </a>
</div>

```python
from machine import Pin, PWM
import time

# Configura los pines para controlar el L298N
l298n_enable = Pin(7, Pin.OUT)  # Conecta a EN del L298N
l298n_input1 = Pin(14, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(9, Pin.OUT)  # Conecta a IN2 del L298N

# Habilita el motor
l298n_enable.on()

# Prepara el PWM
pwm1 = PWM(l298n_input1)
pwm1.freq(1000)

pwm2 = PWM(l298n_input2)
pwm2.freq(1000)

# Define la velocidad del motor (ajusta el valor según sea necesario)
motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)

time.sleep(2)

motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)

time.sleep(2)

l298n_enable.off()

```

Tomando de base los códigos anteriores podemos controlar dos motores DC utilizando el driver L298N a la vez con ayuda del siguiente código, donde se controla la velocidad, dirección y el encendido y apagado de los motores. 


<div style="text-align: right;">
    <a href="/docs/7-Control_de_motores_DC/code/unitRP2040_motors3.py" download="unitRP2040_motors3.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitRP2040_motors3.py
        </button>
    </a>
</div>

```py
from machine import Pin, PWM
import time

# Configura los pines para controlar el L298N
l298n_enableA = Pin(7, Pin.OUT)  # Conecta a ENA del L298N
l298n_input1 = Pin(14, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(9, Pin.OUT)  # Conecta a IN2 del L298N
l298n_enableB = Pin(4, Pin.OUT)  # Conecta a ENB del L298N
l298n_input3 = Pin(8, Pin.OUT)  # Conecta a IN3 del L298N
l298n_input4 = Pin(11, Pin.OUT)  # Conecta a IN4 del L298N

# Habilita el motor
l298n_enableA.on()
l298n_enableB.on()

# Prepara el PWM
pwm1 = PWM(l298n_input1)
pwm1.freq(1000)
pwm2 = PWM(l298n_input2)
pwm2.freq(1000)
pwm3 = PWM(l298n_input3)
pwm3.freq(1000)
pwm4 = PWM(l298n_input4)
pwm4.freq(1000)

# Define la velocidad del motor (ajusta el valor según sea necesario)
motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)
pwm3.duty_u16(motor_speed)
pwm4.duty_u16(0)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)
pwm3.duty_u16(motor_speed)
pwm4.duty_u16(0)

time.sleep(2)

motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)
pwm3.duty_u16(0)
pwm4.duty_u16(motor_speed)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)
pwm3.duty_u16(0)
pwm4.duty_u16(motor_speed)

time.sleep(2)

l298n_enableA.off()
l298n_enableB.off()

```
> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

###  Resultados


![Demo gif](/docs/7-Control_de_motores_DC/images/carrito.gif)

###  Conclusiones
Esta actividad ejemplifica de manera destacada los sistemas de control, al haber desarrollado exitosamente un sistema de control para motores DC. Este logro no solo establece los cimientos para diversos proyectos futuros, sino que también introduce varios conceptos clave de MicroPython, PWM (Modulación de Ancho de Pulso) y un mejor acercamiento a la tarjeta de desarrollo Dual MCU. 




# Continua con el curso [Hilos (THREADS)](/docs/8-hilos/)

* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

#### Referencias
Nise, N. (2019). Control Systems Engineering.v Editorial Wiley.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊

