    ---
title: 10. Control de pantalla OLED (I2C)
type: docs
weight: 10
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 10. Control de pantalla OLED
### 10.1. Objetivo
El objetivo de este proyecto es programar el microcontrolador DualMCU para mostrar información en una pantalla OLED. 

- Mostrar la hora actual en formato de reloj digital.
- Crear un contador regresivo con la capacidad de configurar el tiempo deseado.
- Visualizar datos en tiempo real de sensores ambientales, como temperatura, humedad, calidad del aire, etc.



### 10.2 Requisitos
+ Microcontrolador DualMCU.
+ Pantalla  OLED compatible.
+ Sensores ambientales si se desea mostrar datos en tiempo real.
+ Conexiones eléctricas y fuente de alimentación adecuadas.


### 10.3. Descripción
Este apartado tiene como objetivo proporcionar una plataforma versátil para visualizar datos relevantes en un formato fácilmente comprensible y personalizable.


```py 
'''
Unit Electronics 2023
          (o_
   (o_    //\
   (/)_   V_/_ 
tested code mark
   version: 0.0.1
   revision: 0.0.1

Código de prueba
'''

import machine
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(0,sda=machine.Pin(0), scl=machine.Pin(1))

oled = SSD1306_I2C(128, 32, i2c)

oled.fill(1)
oled.show()

oled.fill(0)
oled.show()
oled.text('UNIT', 50, 10)
oled.text('ELECTRONICS', 25, 20)

oled.show()
```

En la siguente imagen puedes observar el test de prueba funcionando 

![](/docs/10-Control_de_pantalla_OLED/images/oled.jpg)
## Mejora el ejemplo 

```python
from machine import Pin, I2C
import ssd1306
import time

# Inicializar I2C
i2c = machine.I2C(0,sda=machine.Pin(0), scl=machine.Pin(1))
count = 100
segundos = 0
minutos = 15
horas = 10
# Inicializar la pantalla OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def get_current_time():
    global segundos
    global minutos
    global horas
    # Incrementar el contador de segundos
    segundos += 1

    # Verificar si ha pasado un minuto (60 segundos)
    if segundos == 60:
        segundos = 0  # Reiniciar los segundos
        minutos += 1   # Incrementar el contador de minutos

        # Verificar si ha pasado una hora (60 minutos)
        if minutos == 60:
            minutos = 0  # Reiniciar los minutos
            horas += 1    # Incrementar el contador de horas

            # Verificar si ha pasado un día (24 horas)
            if horas == 24:
                horas = 0  # Reiniciar las horas

    return segundos, minutos, horas




def create_countdown():
    global count
    if count <= 0:
        count =100
        raise ValueError("El tiempo del contador debe ser mayor que cero")
    count =count -1
    
    return count

def read_sensor_data():
    # Implementar la función para leer los datos de los sensores ambientales
    pass


# Obtener la hora actual
# Ejemplo de uso


while True:
    sec,minu, hour  = get_current_time()

    # Crear un contador regresivo
    countdown = create_countdown()  # 10 segundos para el ejemplo

    # Leer los datos de los sensores ambientales
    sensor_data = read_sensor_data()

    # Mostrar los datos en la pantalla OLED
    display.fill(0)
    display.text('Hora: '+ str(hour)+":"+str(minu)+":" + str(sec), 0, 0)
    display.text('Contador: ' + str(countdown), 0, 10)
    display.text('Datos del sensor: ' + str(sensor_data), 0, 20)
    display.show()

    time.sleep(1)


```

    1. Inicializar el microcontrolador DualMCU.
    1. Inicializar la pantalla OLED.
    1. Crear una función para obtener la hora actual del sistema y formatearla en formato de reloj digital.
    1. Crear una función para un contador regresivo que acepte un tiempo de entrada.
    1. Inicializar los sensores ambientales.
    1. Crear una función para leer los datos de los sensores ambientales.
    1. Crear una función para mostrar los datos en la pantalla OLED.
![](/docs/10-Control_de_pantalla_OLED/images/oled_hora.gif)
> **Nota:** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Ten en cuenta que este es solo un esquema y necesitarás implementar las funciones `getCurrentTime`, `createCountdown` y `readSensorData` según tus necesidades. También necesitarás incluir las librerías adecuadas para tu microcontrolador y sensores.


## Control para MicroPython SSD1306 OLED
Consideramos una dificultad a la hora de buscar la Biblioteca disponible, por lo que se te proporciona una opcion funcional, copia el codigo y guarda el archivo como **ssd1306.py** en la DualMCU.
```py
# MicroPython SSD1306 OLED driver, I2C and SPI interfaces

from micropython import const
import framebuf


# register definitions
SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_MEM_ADDR = const(0x20)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xA0)
SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_COM_PIN_CFG = const(0xDA)
SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)
SET_CHARGE_PUMP = const(0x8D)

# Subclassing FrameBuffer provides support for graphics primitives
# http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
class SSD1306(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # off
            # address setting
            SET_MEM_ADDR,
            0x00,  # horizontal
            # resolution and layout
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,  # column addr 127 mapped to SEG0
            SET_MUX_RATIO,
            self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # scan from COM[N] to COM0
            SET_DISP_OFFSET,
            0x00,
            SET_COM_PIN_CFG,
            0x02 if self.width > 2 * self.height else 0x12,
            # timing and driving scheme
            SET_DISP_CLK_DIV,
            0x80,
            SET_PRECHARGE,
            0x22 if self.external_vcc else 0xF1,
            SET_VCOM_DESEL,
            0x30,  # 0.83*Vcc
            # display
            SET_CONTRAST,
            0xFF,  # maximum
            SET_ENTIRE_ON,  # output follows RAM contents
            SET_NORM_INV,  # not inverted
            # charge pump
            SET_CHARGE_PUMP,
            0x10 if self.external_vcc else 0x14,
            SET_DISP | 0x01,
        ):  # on
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            # displays with width of 64 pixels are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        self.write_list = [b"\x40", None]  # Co=0, D/C#=1
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.write_list[1] = buf
        self.i2c.writevto(self.addr, self.write_list)


class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):
        self.rate = 10 * 1024 * 1024
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        import time

        self.res(1)
        time.sleep_ms(1)
        self.res(0)
        time.sleep_ms(10)
        self.res(1)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)

```
Archivo fuente original extraido del repositorio [micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306/tree/master)  de [Stefan Lehmann](https://github.com/stlehmann/)

[Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊