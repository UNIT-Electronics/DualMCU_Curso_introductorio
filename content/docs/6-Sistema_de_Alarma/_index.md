---
title: 6. Sistema de alarma (INPUT) 
type: docs
weight: 6
BookToC: false
---

# Prácticas con la DualMCU

## 6. Sistema de alarma
###  Objetivo
Se implementará un sistema capaz de generar una alerta sonora ante la detección de movimiento.

>**NOTA** En esta práctica, se utilizará el **ESP32**.

### 6.2. Descripción
Los sistemas de alarma son fundamentales para mantener seguro un espacio o propiedad. A continuación, te compartimos recursos y código para construir un sistema de alarma personalizado que se adapte a tus necesidades específicas utilizando un dispositivo ESP32 con MicroPython.

###  Requisitos

+ 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
+ 1x <a href="https://uelectronics.com/producto/sensores-de-movimiento-pir-hc-sr501-hc-sr505-hy3612-am312/" target="_blank">Sensores de Movimiento PIR ( HC-SR505)</a>
+ 1x <a href="https://uelectronics.com/producto/buzzer-activo-3v-5v-12v-zumbador/" target="_blank"> Buzzer Activo 3V</a>
+ 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>


### Diagrama de conexión 
A continuación se presenta el diagrama de conexión entre el sensor de movimiento AM312 y la tarjeta de desarrollo.


![](/docs/6-Sistema_de_Alarma/images/DIAGRAMA.jpg)

Adicional, para la realización de la programación de  DualMCU tendrá que encontrarse en la configuración de uso en ESP32
 
<div style="text-align: center;">
<img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
</div>

###  Código
A continuación te presentamos el siguiente programa para manejar el sensor de movimiento AM312  y activar una alarma sonora mediante un buzzer activo.. El código se puede utilizar como punto de partida para crear un sistema de alarma personalizado.

```python
 
from machine import Pin
import time

# Configura el pin del sensor PIR y el buzzer
pir_pin = Pin(16, Pin.IN)  # Reemplaza el número de pin según tu conexión
buzzer_pin = Pin(15, Pin.OUT)  # Reemplaza el número de pin según tu conexión


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


###  Resultados 


Al ejecutar el script , primero se recibirá un mensaje que el sistema está listo para funcionar.
Posteriormente, se recibirá un mensaje de detección a la par que el buzzer activo manda la alerta de movimiento.
 
<div style="text-align: center;">
<img src="/docs/6-Sistema_de_Alarma/images/cap.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

###  Conclusiones

Con este sistema fácilmente se logra reconocer la ubicacion de las terminales de I/O de la tarjeta de desarrollo DualMCU, en su configuración con el ESP32. En donde SE obtiene una señal de entrada por medio del sensor PIR y de esta manera activar un buzzer activo.




> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

# Continua con el curso [Control de Motores](/docs/7-control_de_motores_dc/)



* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.
---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊


