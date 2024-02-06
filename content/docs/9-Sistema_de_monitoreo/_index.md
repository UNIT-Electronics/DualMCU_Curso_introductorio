---
title: 9. Sistema de monitoreo ambiental
type: docs
weight: 9
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 9. Sistema de monitoreo ambiental 
###  Objetivo
Utilizar los sensores DHT11 y MQ135 para medir parámetros ambientales tales como Humedad, temperatura y calidad de aire cada minuto y visualizar las lecturas en el Monitor Serial de Thonny.
>**NOTA** En esta práctica, se utilizará el **ESP32**.


###  Descripción
Los sistemas de control ambiental son fundamentales para medir y gestionar parámetros como la temperatura, humedad, calidad del aire y otros factores para crear entornos cómodos y seguros. A continuación te compartimos recursos y código para construir un sistema de control ambiental utilizando los sensores DHT11 y MQ135 así como la configuración ESP32 con MicroPython.

###  Requisitos
+ 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
+ 1x <a href="https://uelectronics.com/producto/modulo-ky-015-sensor-de-temperatura-y-humedad/" target="_blank">  Detector de Calidad de Aire MQ135</a>
+ 1x <a href="https://uelectronics.com/producto/mq-135-modulo-detector-de-calidad-de-aire/" target="_blank"> Detector de Calidad de Aire MQ135</a>
+ 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>


###  Diagrama de conexión 
A continuación se presenta el diagrama de conexión entre los sensores DHT11 y MQ135 y la tarjeta de desarrollo Dual MCU utilizando el microcontrolador ESP32.

<div style="text-align: center;">
<img src="/docs/9-Sistema_de_monitoreo/images/AR3578Diagrama.jpg" alt="Block Diagram" title="Block Diagram" >
</div>

> **NOTA:** Para la realización de la práctica la Dual MCU tendrá que encontrarse en la configuración de uso en ESP32, dependiendo del código que quieras utilizar.
>       
<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
    </div>

###  Código
```python
'''
Unit Electronics 2024
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
compiler: MicroPython v1.22.0 on 2023-12-27; Generic ESP32 module with ESP32
'''
from dht import DHT11
from machine import Pin, ADC
from time import sleep

sensor = DHT11 (Pin(4))

# configura entrada de adc en el pin 36

adc = ADC(Pin(36))
# configura el rango de lectura de 0 a 3.3v
adc.atten(ADC.ATTN_11DB)
# configura el rango de lectura de 0 a 4095
adc.width(ADC.WIDTH_12BIT)

while True:
  try:
    sleep(2)
    valor = adc.read()
    #imprime el valor del adc
    print(valor)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')
```
###  Resultados 
Este código lee la temperatura y la humedad del sensor DHT11 y la calidad del aire del sensor MQ135 cada minuto, e imprime los valores leídos.


###  Conclusiones

Durante esta práctica, se adquirió conocimiento sobre el funcionamiento de dos sensores, los cuales posibilitan el monitoreo de la temperatura, humedad y calidad del aire. Es imperativo destacar que, además de proporcionar el código y el diagrama de conexiones, se hace necesario llevar a cabo la calibración de los sensores para optimizar su utilidad en una aplicación específica. También es importante señalar la viabilidad de conectar el ESP32 a una red, permitiendo así el envío de las lecturas adquiridas a un servidor o una base de datos.



> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.



# Continua con el curso [Control de LCD o Pantalla OLED](/docs/10-control_de_pantalla_oled/)




* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.
---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊