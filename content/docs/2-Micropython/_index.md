---
title: 2. Micropython y la DualMCU
type: docs
weight: 2
BookToC: false
---
# DualMCU ESP32: MicroPython

Este repositorio contiene un ejemplo básico de cómo instalar MicroPython en la DualMCU utilizando el microcontrolador ESP32. El objetivo principal es que encuentres este repositorio útil y puedas incorporar partes de esta implementación en tus proyectos.
>**NOTA** 
> Recuerda que al trabajar con la DualMCU puedes intercambiar entre micrcontroladores mediante el interruptor de cambios


<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/selector.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

## Configuración del entorno 👋
Antes de comenzar, se recomienda realizar la siguiente configuración:


><a href="https://thonny.org/" target="_blank">Instalación de Thonny </a> Esto te permitirá descargar el firmware en la DualMCU ESP32.




Dirígete a *"Ejecutar"* -> *"Configurar intérprete"*  para completar la configuración.

 ![Interpeter](/docs/2-Micropython/images/config_intepeter.png)

### Actualización de firmware 
Para poder utilizar MicroPython, es recomendable considerar la actualización. Por lo tanto, es necesario iniciar tu DualMCU ESP32 presionando el botón de FLASH.


1. Da clic en "Instalar o Actualizar MicroPython".

1. Se abrirá una nueva ventana. 
    - Se recomienda utilizar la siguiente configuración: 
        - Variant: Espessif ESP32/WROOM
        - Version: 1.20.0

![instalador](/docs/2-Micropython/images/instalador.png)
1. Presionar instalar (esperar a que termine la instalación).


Estos pasos te permitirán actualizar y configurar MicroPython de manera adecuada en tu DualMCU ESP32.


⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊