---
title: 2. Micropython y la DualMCU
type: docs
weight: 2
BookToC: false
---
# DualMCU: MicroPython

Este apartado se presenta un ejemplo básico de cómo instalar MicroPython en la DualMCU utilizando el microcontrolador ESP32 y el RP2040. Nuestra meta principal es que encuentres este recurso útil, permitiéndote integrar partes de esta implementación directamente en tus proyectos.

- [Firmware ESP32](#actualización-de-firmware-esp32)
- [Firmware RP2040](#actualización-de-firmware-rp2040)

A continuación, se proporciona un diagrama de conexión extremadamente sencillo: simplemente conecta la UNIT DUALMCU a tu laptop o computadora de escritorio mediante un cable USB Tipo C. Este paso inicial te permitirá explorar y aprovechar las funcionalidades de MicroPython de manera rápida y eficiente. ¡Esperamos que esta guía simplificada te sea de gran utilidad en tus futuros proyectos!


![pc](/docs/3-Led_intermitente/images/pc_dual.jpg)



Recuerda que al trabajar con la DualMCU puedes intercambiar entre micrcontroladores mediante el interruptor de cambios


<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/selector.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>







## Configuración del entorno👋
Antes de comenzar, se recomienda realizar la siguiente configuración:


><a href="https://thonny.org/" target="_blank">Instalación de Thonny </a> Esto te permitirá descargar el firmware en la DualMCU ESP32.


Dirígete a *"Ejecutar"* -> *"Configurar intérprete"*  para completar la configuración.


<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/find.png" alt="Block Diagram" title="Block Diagram" >
</div>

>**NOTA**
>Encaso de que la `UNIT DUALMCU ESP32` no sea reconocida será necesario instalar el [controlador CH340](/docs/3-Led_intermitente/images/CH341SER.EXE). 


Al hacerlo, se abrirá la siguiente ventana,


<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/config_intepeter.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>



### Actualización de firmware ESP32
Iniciar la UNIT DualMCU con el microcontrolador ESP32 **Posición A**, presionando el botón de FLASH y conectando el dispositivo a la pc. 

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/flash.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>


1. Da clic en **"Instalar o Actualizar MicroPython"**.

1. Se abrirá una nueva ventana. 
    - Se recomienda utilizar la siguiente configuración: 
        - Variant: Espessif ESP32/WROOM
        - Version: 1.20.0

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/instalador.png" alt="Block Diagram" title="Block Diagram" >
</div>

3. Presionar instalar (esperar a que termine la instalación).



Selecciona la tarjeta con la que deseas trabajar en la parte inferior de Thonny. Puedes encontrar esta opción en un formato similar al que se muestra en la siguiente imagen para el ESP32. Ten en cuenta que el puerto COM es asignado por la máquina y puede variar.

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/target.png" alt="Block Diagram" title="Block Diagram" >
</div>




### Actualización de firmware RP2040
Iniciar la UNIT DualMCU con el microcontrolador RP2040  **Posición B**, presionando el botón de `BOOT` y conectando el dispositivo a la pc. 

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/RP2040-Boot_button.jpg" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>


1. Da clic en **"Instalar o Actualizar MicroPython"**.

1. Se abrirá una nueva ventana. 
    - Se recomienda utilizar la siguiente configuración: 
        - Variant: Raspberry Pi Pico/Pico H
        - Version: 1.22.2

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/config_intepeter_rp.png" alt="Block Diagram" title="Block Diagram" >
</div>

3. Presionar instalar (esperar a que termine la instalación).



Selecciona la tarjeta con la que deseas trabajar en la parte inferior de Thonny. Puedes encontrar esta opción en un formato similar al que se muestra en la siguiente imagen para el RP2040. Ten en cuenta que el puerto COM es asignado por la máquina y puede variar.

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/target_rp.png" alt="Block Diagram" title="Block Diagram" >
</div>



## Carga tu primer "Hola Mundo" 🌎
Una vez que el dispositivo ha sido configurado para la prueba, se recomienda generar tu primer "Hola Mundo", ya que los siguientes códigos de las prácticas seguirán el siguiente formato.

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/explorando.png" alt="Block Diagram" title="Block Diagram" style="width: 800px;">
</div>


Copia el código proporcionado:

```py
print("Hola, mundo!")

```

**Ejecuta el código**. Puedes encontrar un botón verde en la parte superior:


<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/buton.png" alt="Block Diagram" title="Block Diagram">
</div>

Visualiza el resultado en la terminal serial:

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/result.png" alt="Block Diagram" title="Block Diagram">
</div>

Este sencillo paso te introduce en el entorno MicroPython y establece las bases para las prácticas siguientes. ¡Explora y disfruta tu experiencia de programación en MicroPython!







# Continua con el curso [LED Intermitente](/docs/3-led_intermitente/)


⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊