---
title: 3. Led intermitente (OUTPUT) 
type: docs
weight: 3
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 3. Led intermitente
###  Objetivo
El objetivo principal de esta sección es desarrollar las habilidades necesarias para programar un efecto de parpadeo intermitente, comúnmente conocido como "Blink", a una frecuencia específica. 

 >**NOTA** En esta práctica, se emplearán ambos microcontroladores para fortalecer los fundamentos básicos.

###  Descripción
La realización de un programa sencillo del parpadeo de un LED se encuentra respaldada por diversos propósitos beneficiosos. Entre ellos, se destaca la verificación del funcionamiento inicial de la DUALMCU, el entendimiento de la estructura del programa para cada microcontrolador, la familiarización con el entorno de programación y el hardware asociado a la DUALMCU. Esta práctica inicial sienta las bases esenciales para abordar con éxito las siguientes actividades.

El procedimiento para llevar a cabo esta práctica implica la utilización de los dos LEDs RGB incorporados en la placa de desarrollo UNIT DUALMCU. La configuración y programación de ambos microcontroladores se realizarán de manera coordinada, permitiendo así lograr el efecto deseado de parpadeo intermitente. Esta práctica no solo proporciona una introducción práctica al manejo de LEDs y programación, sino que también establece una base sólida para futuras actividades prácticas en este entorno de desarrollo específico



### Requisitos

En la presente práctica, los componentes electrónicos necesarios ya están integrados en su totalidad en la placa de desarrollo. Para llevar a cabo la implementación del programa, se emplearán dos LEDs RGB. A continuación, se detallan los materiales específicos que se utilizarán en esta actividad
- <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
- <a href="https://uelectronics.com/producto/cable-usb-tipo-c-3a-6a/" target="_blank">Cable USB Tipo C</a>

### Diagrama de Conexión
A continuación, se muestra el diagrama de conexión, el cual es muy sencillo: solo necesitas conectar la UNIT DUALMCU a tu laptop o computadora de escritorio mediante un cable USB Tipo C.


![pc](/docs/3-Led_intermitente/images/pc_dual.jpg)

### Software
Después de conectar la UNIT DUALMCU al ordenador, procede a encender el dispositivo y seleccionar el microcontrolador (MCU) deseado.
       <div style="text-align: center;">
       <img src="/docs/2-Micropython/images/esp32_or_rasp.jpg" alt="Block Diagram" title="Block Diagram" style="width: 300px;">
       </div>

>**NOTA**
>Encaso de que la UNIT DUALMCU no sea reconocida será necesario instalar el [controlador CH340](/docs/3-Led_intermitente/images/CH341SER.EXE). Este controlador es crucial para establecer la comunicación y la programación con el MCU ESP32. 

### Código
Usa el siguiente código para comprobar el fucionamiento de la instalación del firmware de micropython. Asegúrate de tener seleccionado el MCU ESP32 y carga el siguiente código. 

```py
'''
Unit Electronics 2023
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.1
   revision: 0.0.1
'''
import machine
import time

led_pin = machine.Pin(4, machine.Pin.OUT)
led_pin2 = machine.Pin(26, machine.Pin.OUT)
led_pin3 = machine.Pin(25, machine.Pin.OUT)


def loop():
     while True:
        led_pin.on()    
        led_pin2.on()   
        led_pin3.on()  
        time.sleep(1)  
        led_pin.off()   
        led_pin2.off()  
        led_pin3.off()  
        time.sleep(1)   

loop()
```


El código proporcionado tiene como objetivo probar la configuración de la instalación de MicroPython en el ESP32. Este código enciende los tres LEDs y luego los apaga en un intervalo de 1 segundo. Puedes personalizar el código para ajustar la frecuencia del parpadeo del LED. Por ejemplo, al modificar el valor dentro de la función 'time.sleep(1)' a 'time.sleep(0.5)', el LED parpadeará cada 0.5 segundos en lugar de 1 segundo. Se muestra a continuación el funcionamiento: 
### Resultados
Se puede visualizar el funcionamiento en el siguiente gif:

![](/docs/3-Led_intermitente/images/blink_led2.gif)

### Interactua con el RP2040
1. Asegúrate de que el selector de posición esté configurado para el RP2040 en la UNIT DUALMCU.

1. Actualiza el puerto serial COM de acuerdo con la configuración de tu sistema operativo.

1. Abre Thonny y copia el código proporcionado a continuación.

1. Pega el código en Thonny y ejecútalo para visualizar el comportamiento del LED correspondiente al RP2040.
```py
'''
Unit Electronics 2023
       (o_
(o_    //\
(/)_   V_/_ 
'''
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)  # Configura el pin GPIO25 como salida

while True:
    led.value(not led.value())  # Invierte el estado del LED (encendido/apagado)
    utime.sleep(1)  # Espera 1 segundo
```


### Conclusiones
Esta práctica del Blink en la UNIT DUALMCU no solo ha sido una introducción útil para programar los MCUs RP2040, ESP32 y el manejo de la placa con MicroPython, sino que también nos ha proporcionado una base sólida para explorar y expandir nuestros conocimientos y habilidades para concretar las siguientes prácticas que se llevarán acabo como para futuros proyectos con la placa DUALMCU.


> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.


# Continua con el curso [Sensor de Temperatura](/docs/4-sensor_de_temperatura/)

* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.
---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊