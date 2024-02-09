---
title: 8. Hilos (THREADS)
type: docs
weight: 8
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 8. Hilos (threads)
###	 Objetivo
 
Comprender el funcionamiento de hilos en el microcontrolador ESP32.

>**NOTA** En esta práctica, se utilizará el **ESP32**.


###	 Descripción

Los hilos, también conocidos como threads en inglés, son una forma poderosa de realizar múltiples tareas de manera concurrente en un programa de software. En MicroPython, los hilos nos permiten dividir la ejecución de nuestro programa en múltiples secuencias de instrucciones, lo que puede mejorar significativamente la eficiencia y la capacidad de respuesta de nuestras aplicaciones en plataformas como DualMCU ESP32.

El código proporcionado implementa dos hilos en MicroPython para el ESP32. Un hilo incrementa una variable compartida, mientras que el otro hilo imprime el valor compartido. Esto sirve como un ejemplo básico de cómo trabajar con hilos en MicroPython.

>**NOTA** 
> Recuerda que al trabajar con la DualMCU puedes intercambiar entre micrcontroladores mediante el interruptor de cambios, para esta práctica utilizaremos sólo el microcontrolador **ESP32** por lo que debes cambiar el interruptor a la posición “B”.”

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/selector.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

###	 Requisitos

En la presente práctica, los componentes electrónicos se encuentran integrados en la placa de desarrollo.
- <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
- <a href="https://uelectronics.com/producto/cable-usb-tipo-c-3a-6a/" target="_blank">Cable USB Tipo C</a>

### Diagrama de conexión 
![pc](/docs/3-Led_intermitente/images/pc_dual.jpg)
###  Codigo

El código crea dos hilos: uno para incrementar una variable compartida y otro para imprimir el valor compartido.

Los hilos se ejecutan durante 10 segundos antes de finalizar.

```py
'''
Unit Electronics 2023
        >o)
        (_>
file: share_data.py
author: Cesar
version: 0.0.1
revision: 0.0.1
context: This code facilitates the sharing of data within a counter through the utilization of threads.

ESP32
'''
import _thread
import time

shared_variable = 0

def increment_thread():
    global shared_variable
    for _ in range(10):
        shared_variable += 1
        time.sleep(1)

def print_thread():
    global shared_variable
    for _ in range(10):
        print("Valor compartido:", shared_variable)
        time.sleep(1)

# Crear y lanzar los hilos
_thread.start_new_thread(increment_thread, ())
_thread.start_new_thread(print_thread, ())

time.sleep(10)

```

## Resultados
En la imagen proporcionada a continuación, se presenta una captura de pantalla de la salida obtenida al utilizar hilos. La representación visual ofrece una visión más concreta de cómo los hilos están interactuando y compartiendo datos durante la ejecución del código.

![pc](/docs/8-Hilos/images/shell.png)



###	Conclusión 

El código demostrativo para MicroPython en ESP32 muestra la implementación de hilos para facilitar el intercambio de datos concurrente. La funcionalidad principal se centra en dos hilos: uno para incrementar una variable compartida y otro para imprimir ese valor. Este ejemplo básico ofrece una introducción práctica al uso de hilos en un entorno MicroPython.
# Continua con el curso [Sistema de Monitoreo Ambiental](/docs/9-sistema_de_monitoreo/)

* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊