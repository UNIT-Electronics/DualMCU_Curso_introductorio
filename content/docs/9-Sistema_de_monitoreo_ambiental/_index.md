---
title: 9. Sistema de monitoreo ambiental
type: docs
weight: 9
BookToC: false
---

# Prácticas con la DualMCU

## 9. Sistema de monitoreo ambiental
### 9.1. Objetivo
Utiliza sensores para medir parámetros ambientales como
temperatura, humedad, calidad del aire, etc. Los datos pueden ser registrados y enviados a un servidor
a través de una conexión inalámbrica.

### 9.2. Descripción
Este repositorio contiene un conjunto de recursos y código para construir un sistema de control ambiental utilizando un dispositivo ESP32 o RP2040 con MicroPython. Los sistemas de control ambiental son fundamentales para medir y gestionar parámetros como la temperatura, humedad, calidad del aire y otros factores para crear entornos cómodos y seguros.

```python

import machine
import time


```


### 9.3 Contenido del Repositorio
Código Fuente: En este repositorio, encontrarás el código fuente necesario para monitorear y controlar parámetros ambientales. Se proporcionarán ejemplos de código que demuestran cómo utilizar sensores para medir temperatura, humedad, calidad del aire y otros factores.

**Diagramas de Conexión:** Se incluirán diagramas de conexión que detallan cómo conectar sensores y actuadores a tu ESP32 o RP2040 para crear un sistema de control ambiental.

**Instrucciones de Uso:** Las instrucciones detalladas te guiarán a través del proceso de configuración y ejecución del sistema de control ambiental. También se proporcionarán detalles sobre cómo personalizar la configuración y visualizar los datos recopilados.

**Recursos Adicionales:** Se pueden incluir enlaces a recursos adicionales, como tutoriales sobre el uso de sensores específicos y consejos para mejorar la calidad del aire.

### 9.4 Instrucciones de Uso
1. Clona o descarga este repositorio en tu entorno de desarrollo de MicroPython.

1. Sigue las instrucciones de conexión para conectar sensores de temperatura, humedad, calidad del aire y otros componentes a tu ESP32 o RP2040.

1. Abre el código fuente en tu entorno de desarrollo MicroPython y carga el código en tu placa de desarrollo.

1. Ejecuta el código en tu placa de desarrollo y comienza a recopilar datos ambientales.

Utiliza las instrucciones proporcionadas para visualizar y analizar los datos recopilados, o para activar actuadores (como sistemas de aire acondicionado o purificadores de aire) según los valores ambientales.

### 9.5 Requisitos
+ Placa de desarrollo compatible con MicroPython (ESP32 o RP2040).
+ Sensores de temperatura, humedad, calidad del aire, u otros sensores ambientales según tus necesidades.
+ Actuadores si deseas realizar cambios en el ambiente en función de los datos recopilados.
+ Conexiones eléctricas y fuente de alimentación adecuadas.