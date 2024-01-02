---
title: 8. Termostato inteligente
type: docs
weight: 8
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 8. Termostato inteligente
### 8.1. Objetivo
El objetivo de este proyecto es utilizar el microcontrolador DualMCU para crear un termostato inteligente que pueda:

### 8.1.1 Medir la temperatura ambiente con precisión.
- Controlar un sistema de calefacción o refrigeración para mantener la temperatura dentro del rango deseado.
- Ser eficiente en el consumo de energía y capaz de funcionar de manera autónoma.
### 8.2 Contenido del Repositorio
Código Fuente: Este repositorio incluirá el código fuente necesario para implementar las funciones de medición de temperatura y control del sistema de calefacción o refrigeración. Se proporcionarán ejemplos de código que demuestran cómo utilizar las capacidades del DualMCU.


### 8.3. Descripción
Este repositorio contiene un conjunto de recursos y código para crear un termostato inteligente utilizando un microcontrolador DualMCU. Un termostato inteligente es una solución eficiente para controlar la temperatura de un espacio y mantenerla dentro de un rango deseado. Este proyecto te permitirá medir la temperatura ambiente y controlar sistemas de calefacción o refrigeración de manera automática.

### 8.4 Requisitos
+ 1x Placa de desarrollo [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ 1x [Sensor de temperatura LM35](https://uelectronics.com/producto/lm35-sensor-de-temperatura/)
+ Actuadores para calefacción o refrigeración. [Celda Peltier TEC1-12706 12v 60W](https://uelectronics.com/producto/celda-peltier/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.

**Placa de desarrollo DualMCU:** Esta placa es el cerebro de nuestro termostato inteligente. Es responsable de procesar los datos del sensor de temperatura y controlar los actuadores.

**Sensor de temperatura LM35:** Este sensor es capaz de medir la temperatura ambiente con alta precisión. Los datos recogidos por este sensor serán utilizados por la placa DualMCU para controlar los actuadores.

**Actuadores para calefacción o refrigeración:** En este caso, vamos a utilizar una Celda Peltier TEC1-12706 12v 60W. Este dispositivo puede enfriar o calentar un espacio dependiendo de la corriente eléctrica que se le aplique.

**Conexiones eléctricas y fuente de alimentación adecuadas:** Necesitarás varios cables para conectar todos los componentes entre sí. Además, necesitarás una fuente de alimentación que pueda proporcionar la cantidad adecuada de energía a tu termostato inteligente.

```python
from machine import Pin, ADC
import time

# Configura el sensor LM35
lm35 = ADC(Pin(36))

# Configura el controlador H-bridge
hbridge_in1 = Pin(12, Pin.OUT)
hbridge_in2 = Pin(13, Pin.OUT)

# Temperatura objetivo
target_temp = 25.0

while True:
    # Lee la temperatura del sensor LM35
    temp = lm35.read() * 3.3 / 4095 * 100

    # Controla la celda Peltier en función de la temperatura
    if temp < target_temp:
        # Enciende la celda Peltier para calentar
        hbridge_in1.on()
        hbridge_in2.off()
    else:
        # Enciende la celda Peltier para enfriar
        hbridge_in1.off()
        hbridge_in2.on()

    # Espera un minuto antes de la próxima lectura
    time.sleep(60)
```
> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

En termostato real tendría características adicionales, como la capacidad de ajustar la temperatura objetivo a través de una interfaz de usuario, y podría implementar un algoritmo más sofisticado para controlar el sistema de calefacción o refrigeración de manera más eficiente.


* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊