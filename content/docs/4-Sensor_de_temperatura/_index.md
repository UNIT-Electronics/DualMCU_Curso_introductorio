---
title: 4.  Sensor de termperatura (ADC)
type: docs
weight: 4
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 4. Sensor de temperatura
###  Objetivo
Obtener las lecturas de la temperatura actual mediante un sensor analógico LM35 y visualizar los resultados a través del monitor en serie del IDE de Thonny.

>**NOTA** En esta práctica, se utilizará el **RP2040**.


###  Descripción

En esta práctica, nos enfocaremos en la utilización del sensor analógico LM35 para la medición de la temperatura actual. El sensor LM35 ha sido seleccionado debido a su versatilidad y su capacidad para integrarse fácilmente con diversas placas de desarrollo. Este componente se presenta como una opción idónea para entornos educativos y proyectos de electrónica, ya que es compatible con una amplia variedad de plataformas, tales como Arduino, Raspberry Pi, Nodemcu, ESP32, así como otros dispositivos que cuenten con pines analógicos.

La elección del LM35 se fundamenta en su precisión en la medición de temperatura y su sencillo método de conexión. Al ser un sensor analógico, brinda lecturas continuas y proporciona una interfaz amigable con los microcontroladores mencionados, facilitando su integración en proyectos de monitoreo ambiental, control climático, y otros que requieran mediciones térmicas en tiempo real.

Esta práctica, además de brindar la oportunidad de familiarizarse con el manejo del sensor LM35, ofrece un punto de partida para comprender cómo realizar lecturas analógicas y visualizar los resultados a través del monitor en serie del IDE de Thonny. El código de ejemplo proporcionado permitirá a los usuarios implementar esta funcionalidad tanto en dispositivos ESP32 como en RP2040, utilizando el entorno de ejecución MicroPython. Este enfoque flexible hace que la práctica sea accesible y adaptable a diversas plataformas, contribuyendo así a la versatilidad y aplicabilidad del conocimiento adquirido. 

### Descripción del ADC
El uso de la clase ADC ofrece una interfaz para los convertidores analógico-digital y se presenta como un punto final singular capaz de capturar y transformar un voltaje continuo en un valor digital discretizado. La clase ADC se encuentra dentro del módulo machine y se puede importar de la siguiente manera:

```python
from machine import ADC

adc = ADC(pin)        # create an ADC object acting on a pin
val = adc.read_u16()  # read a raw analog value in the range 0-65535
val = adc.read_uv()   # read an analog value in microvolts
```
- Para mayor información puedes consultar la [Documentación oficial de MicroPython](https://docs.micropython.org/en/latest/library/machine.ADC.html).
- Tambien puedes consultar el ejemplo displonible para el ADC del [repositorio de la DualMCU](https://github.com/UNIT-Electronics/DualMCU/blob/main/Examples/Micropython%20Basics/RP2040/01.ADC/ADC.py).



###  Materiales

- 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
- 1x <a href="https://uelectronics.com/producto/lm35-sensor-de-temperatura/" target="_blank">Sensor de temperatura LM35</a>
- 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>

Para utilizar el microcontrolador ESP32 necesitarás adicionalmente a los materiales mencionados anteriormente:
- 2x <a href="https://uelectronics.com/producto/led-5mm-difuso-rojo-amarillo-verde-azul-blanco/" target="_blank">LEDs </a>
- 2x <a href="https://uelectronics.com/producto/resistencia-1-4w-presicion/" target="_blank">Resistencias 220Ω</a>



###  Diagrama de conexión 
>**NOTA** 
> Recuerda que al trabajar con la DualMCU puedes intercambiar entre micrcontroladores mediante el interruptor de cambios

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/selector.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>
A continuación, se presenta el diagrama de conexión entre el sensor de temperatura LM35 y la tarjeta de desarrollo Dual MCU utilizando el microcontrolador RP2040.


![](/docs/4-Sensor_de_temperatura/images/AR3578_Diagrama_RP2.jpg)

Si quieres realizar la práctica utilizando el microcontrolador ESP32 utiliza el siguiente diagrama:

![](/docs/4-Sensor_de_temperatura/images/AR3578_Diagrama_ESP2.jpg)

####  Código
Estos dos códigos muestran ejemplos de cómo utilizar el sensor de temperatura LM35 con dos microcontroladores diferentes: el RP2040 y el ESP32. En ambos casos, se configura la entrada analógica para leer la salida del LM35 y se realiza la lectura de la temperatura en grados Celsius.

<div style="text-align: right;">
    <a href="/docs/4-Sensor_de_temperatura/code/unitESP32_adc.py" download="unitRP2040_adc.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitRP2040_adc.py
        </button>
    </a>
</div>

```python
'''
Unit Electronics 2024
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.1
   revision: 0.0.1
    RP2040 
'''
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

El código para el RP2040 utiliza MicroPython y Thonny para imprimir las lecturas de temperatura en el monitor serial. Se configura el pin de entrada analógica, se lee el valor del LM35 en milivoltios, se convierte a grados Celsius y se imprime en el formato deseado. El bucle infinito asegura que las lecturas se realicen continuamente con un intervalo de espera de un segundo.

<div style="text-align: right;">
    <a href="/docs/4-Sensor_de_temperatura/code/unitESP32_adc.py" download="unitESP32_adc.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitESP32_adc.py
        </button>
    </a>
</div>

```python
'''
Unit Electronics 2024
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
ESP32
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
Por otro lado, el código para el ESP32 también configura la entrada analógica para el pin específico, pero en este caso, además de imprimir las lecturas en el monitor serial, se utiliza la información para controlar dos LEDs. Dependiendo de si la lectura es mayor o menor a 2000, se encienden o apagan los LEDs, proporcionando una respuesta visual. El bucle infinito asegura la repetición continua de la lectura y el control de los LEDs con un intervalo de espera de un segundo. Este código ilustra cómo se puede utilizar la información del sensor para realizar acciones visuales adicionales.

## Resultados

Puede apreciar dentro de tu monitor serie, el valor de la temperatura en grados centigrados.
![](/docs/4-Sensor_de_temperatura/images/sensor.png)

## Conclusiones 
En conclusión, la práctica ha permitido adquirir conocimientos prácticos sobre la lectura de sensores analógicos de temperatura y la configuración del ADC en microcontroladores. Además, se ha demostrado cómo estos microcontroladores pueden no solo leer datos, sino también interactuar con dispositivos externos, como LEDs, para proporcionar una respuesta visual en función de las lecturas obtenidas. Este aprendizaje es fundamental para el desarrollo de proyectos que involucren la medición y control de variables analógicas en entornos electrónico





> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

# Continua con el curso [Control de Servo](/docs/5-control_servo/) 

* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊