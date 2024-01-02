---
title: 4.  Sensor de termperatura (ADC)
type: docs
weight: 4
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 4. Sensor de temperatura
### 4.1. Objetivo
Conectar un sensor de temperatura (como el LM35) al microcontrolador y
programar para que muestre la temperatura actual en un monitor serie. Esto te
ayudará a trabajar con sensores analógicos y a interpretar datos de sensores.

### 4.2. Descripción

Este apartado incluye informacion aplicable para el ESP32 y el RP2040. Cada archivo se puede correr bajo el nombre de **sensor.py** que puedes cargar en la respectiva placa para hacer que lea por ADC, información de temperatura.

El sensor LM35 se caracteriza por su sencillez de uso, ya que no requiere de la implementación de circuitos adicionales para su operación. Su conexión se reduce a la vinculación del pin de alimentación (+V) con una fuente de voltaje de 5V, la conexión del pin de tierra (GND) a la referencia de tierra (0V), y la interconexión del pin de salida de datos (VOUT) con un puerto analógico. Esta versatilidad de conexión lo hace compatible con una amplia gama de microcontroladores, incluyendo, pero no limitándose a placas de desarrollo Arduino, Raspberry Pi, Nodemcu, ESP32, así como con cualquier otro dispositivo que disponga de pines analógicos. Si requieres de mayor información sobre el sensor, puedes consultar la [Documentación](https://uelectronics.com/producto/lm35-sensor-de-temperatura/).

### Materiales

+ 1x [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ 1x [Sensor de temperatura LM35](https://uelectronics.com/producto/lm35-sensor-de-temperatura/)


El uso de la clase ADC ofrece una interfaz para los convertidores analógico-digital y se presenta como un punto final singular capaz de capturar y transformar un voltaje continuo en un valor digital discretizado. La clase ADC se encuentra dentro del módulo machine y se puede importar de la siguiente manera:

```python
from machine import ADC

adc = ADC(pin)        # create an ADC object acting on a pin
val = adc.read_u16()  # read a raw analog value in the range 0-65535
val = adc.read_uv()   # read an analog value in microvolts
```
- Para mayor información puedes consultar la [Documentación oficial de MicroPython](https://docs.micropython.org/en/latest/library/machine.ADC.html).
- Tambien puedes consultar el ejemplo displonible para el ADC del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/01.ADC/ADC.py).
```python
'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
context: This code is a basic configuration of a ADC
'''
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
Y aquí tienes un ejemplo similar para el RP2040:

```python
import machine
import time

# Configura el pin de entrada analógica para leer la salida del LM35
pin_lm35 = machine.Pin(28, machine.Pin.IN)
adc = machine.ADC(pin_lm35)

while True:
    # Lee el valor del sensor LM35 en milivoltios
    lm35_output_mv = adc.read_u16() * 3.3 / 65535  * 1000
    
    # Convierte el valor a grados Celsius usando la fórmula
    temperatura_celsius = (lm35_output_mv - 500) / 10
    
    # Imprime la temperatura en grados Celsius
    print("Temperatura: {:.2f} °C".format(temperatura_celsius))
    
    # Espera un segundo antes de tomar la siguiente lectura
    time.sleep(1)


```
Puedea apreciar dentro de tu monitor serie, el valor de la temperatura en grados centigrados.
![](/docs/4-Sensor_de_temperatura/images/sensor.png)

> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊