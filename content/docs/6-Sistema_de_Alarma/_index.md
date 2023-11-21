---
title: 6. Sistema de alarma (INPUT) 
type: docs
weight: 6
BookToC: false
---

# Prácticas con la DualMCU

## 6. Sistema de alarma
### 6.1. Objetivo
Crear un sistema de alarma utilizando un microcontrolador y un sensor de
movimiento. Cuando se detecte movimiento, el sistema puede activar una alarma sonora.

### 6.2. Descripción
La documentación presente contiene un conjunto de recursos y código para construir un sistema de detección utilizando un dispositivo ESP32 o RP2040 con MicroPython. Los sistemas de alarma son fundamentales para mantener seguro un espacio o propiedad. Con MicroPython, puedes crear un sistema de alarma personalizado que se adapte a tus necesidades específicas.

### 6.3 Requisitos
+ 1x Placa de desarrollo [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/)
+ 1x [Sensores de Movimiento PIR (HC-SR501 / HC-SR505 / HY3612 / AM312)](https://uelectronics.com/producto/sensores-de-movimiento-pir-hc-sr501-hc-sr505-hy3612-am312/)
+ 1x [Buzzer Zumbador 5V Pasivo](https://uelectronics.com/producto/buzzer-zumbador-5v-pasivo/)
+ Conexiones eléctricas y fuente de alimentación adecuadas.

### 6.4 Contenido del Repositorio
**Código Fuente:** En este apartado, encontrarás el código fuente necesario para manejar el sensor de movimiento y activar una alarma sonora. El código se puede utilizar como punto de partida para crear un sistema de alarma personalizado.

```python
 
from machine import Pin
import time

# Configura el pin del sensor PIR y el buzzer
pir_pin = Pin(12, Pin.IN)  # Reemplaza el número de pin según tu conexión
buzzer_pin = Pin(13, Pin.OUT)  # Reemplaza el número de pin según tu conexión

# Función para activar la alarma
def activate_alarm():
    print("¡Movimiento detectado! Activando alarma...")
    buzzer_pin.on()
    time.sleep(5)  # La alarma suena durante 5 segundos
    buzzer_pin.off()

print("Sistema de alarma PIR activado")

while True:
    if pir_pin.value() == 1:  # El sensor PIR detecta movimiento
        activate_alarm()
    
    time.sleep(0.5)  # Espera 0.5 segundos antes de volver a verificar el sensor PIR



```
> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

**Recursos Adicionales:**


Puedes mejorar tu habilidad complemtando el siguiente proyecto: [DualMCU_ESP32_Panel_de_control_Web](https://github.com/UNIT-Electronics/DualMCU_ESP32_Panel_de_control_Web)




