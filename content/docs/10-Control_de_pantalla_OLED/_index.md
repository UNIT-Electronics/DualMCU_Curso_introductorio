    ---
title: 10. Control de pantalla OLED (I2C)
type: docs
weight: 10
BookToC: false
---

# Prácticas con la DualMCU - MicroPython

## 10. Control de pantalla OLED
### Objetivo
El objetivo de este proyecto es usar el microcontrolador DualMCU para mostrar información en una pantalla OLED.

>**NOTA** En esta práctica, se utilizará el **ESP32**.

###  Descripción
Visualizamos datos relevantes en un formato fácilmente comprensible y personalizable por medio de una pantalla OLED en 3 diferentes fases:

1. Carga de la librería para el uso de la pantalla OLED SSD1306 
2. Mostrar información tipo texto en la pantalla
3. Crear un contador regresivo con la capacidad de configurar el tiempo deseado y visualizar datos en tiempo real de sensores ambientales, puedes utilizar los sensores de las anteriores prácticas como;temperatura, humedad, calidad del aire, etc. 

Cabe mencionar que se usará comunicación I2C como protocolo de comunicación entre la pantalla OLED y la DUAL MCU ; la propuesta es que puedas utilizar cualquier sensor para poder mostrar el dato en la misma pantalla, ya sea de los sensores de las prácticas anteriores o uno nuevo.




###  Requisitos
+ 1x <a href="https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/" target="_blank">Placa UNIT  DualMCU</a>
+ 1x <a href="https://uelectronics.com/producto/display-oled-azul-y-blanco-128x64-0-96-i2c-ssd1306/" target="_blank">  Pantalla  OLED</a>
+ 1x <a href="https://uelectronics.com/producto/protoboard-400-pts/" target="_blank"> 	Protoboard </a>
+ 1x <a href="https://uelectronics.com/producto/65-cables-para-protoboard-macho/" target="_blank">	Cables para protoboard </a>
+ 1x <a href="https://uelectronics.com/producto/cables-dupont-largos-20cm-hh-mh-mm/" target="_blank">Cables Dupont : Hembra - Macho</a>


###  Diagrama de conexión 


>**NOTA** 
> Recuerda que al trabajar con la DualMCU puedes intercambiar entre micrcontroladores mediante el interruptor de cambios, para esta práctica utilizaremos sólo el microcontrolador **ESP32** por lo que debes cambiar el interruptor a la posición “B”.”

<div style="text-align: center;">
    <img src="/docs/2-Micropython/images/selector.png" alt="Block Diagram" title="Block Diagram" style="width: 600px;">
</div>

El siguiente diagrama es para tener comunicación entre ambos módulos y poder mostrar un texto predeterminado.

<div style="text-align: center;">
<img src="/docs/10-Control_de_pantalla_OLED/images/OLED1.jpg" alt="Block Diagram" title="Block Diagram" >
</div>

Otra opción de conexión es directamente en los pines de comunicación I2C QWIIC para ESP32.

<div style="text-align: center;">
<img src="/docs/10-Control_de_pantalla_OLED/images/qwiic.png" alt="Block Diagram" title="Block Diagram" style="width: 200px;">
</div>

###  Software
Para facilitar la programación con la pantalla OLED, hemos identificado una librería específica para OLED. Te proporcionamos una alternativa práctica: copia el código y guarda el archivo como **ssd1306.py** en la DualMCU.
<div style="text-align: right;">
    <a href="/docs/10-Control_de_pantalla_OLED/code/ssd1306.py" download="ssd1306.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download ssd1306.py
        </button>
    </a>
</div>


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
> **NOTA** Archivo fuente original extraido del repositorio [micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306/tree/master)  de [Stefan Lehmann](https://github.com/stlehmann/)

Posteriormente guarda el anterior código en la Dual MCU bajo el nombre de **ssd1306.py**


<div style="text-align: center;">
    <img src="/docs/10-Control_de_pantalla_OLED/images/OLED_V2.jpg" alt="Block Diagram" title="Block Diagram" >
    </div>


###  Código

Una vez guardado el programa anterior, procederemos a abrir un nuevo programa y realizar el siguiente código que tiene como finalidad la visualización de la leyenda **“UNIT ELECTRONCS”**

<div style="text-align: right;">
    <a href="/docs/10-Control_de_pantalla_OLED/code/unitRP2040_oled.py" download="unitRP2040_oled.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitRP2040_oled.py
        </button>
    </a>
</div>

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
from ssd1306 import SSD1306_I2C

i2c = machine.I2C(sda=machine.Pin(22), scl=machine.Pin(21)))

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

<div style="text-align: center;">
<img src="/docs/10-Control_de_pantalla_OLED/images/oled.jpg" alt="Block Diagram" title="Block Diagram" style="width: 500px;">
</div>


>**NOTA** Ten en cuenta que este código es un ejemplo y puede que necesites ajustarlo según tu configuración específica y tus necesidades.

Ahora será tú turno de desplegar información proveniente de algún sensor, adicional te compartimos un código en donde podrás  obtener las siguientes funciones:
1. El despliegue de la  hora actual del sistema y formatearla en formato de reloj digital.
1. Crear una función para un contador regresivo que acepte un tiempo de entrada.
1. Inicializar, contar con lectura los sensores ambientales (que tu propongas) y mostrar los datos en pantalla.

Ten en cuenta que este es solo un esquema y necesitarás implementar las funciones `getCurrentTime`, `createCountdown` y `readSensorData` según tus necesidades. También necesitarás incluir las librerías adecuadas para tu microcontrolador y sensores.


<div style="text-align: right;">
    <a href="/docs/10-Control_de_pantalla_OLED/code/unitRP2040_oled2.py" download="unitESP32_oled2.py">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            Download unitESP32_oled2.py
        </button>
    </a>
</div>

```python
from machine import Pin, I2C
import ssd1306
import time

# Inicializar I2C
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
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
<div style="text-align: center;">
<img src="/docs/10-Control_de_pantalla_OLED/images/oled_hora.gif" alt="Block Diagram" title="Block Diagram" >
</div>

### Conclusiones
Durante el desarrollo de la práctica, se evidenció con éxito la configuración de la comunicación I2C con la pantalla OLED, destacando la importancia de emplear una librería compatible con el dispositivo utilizado. Es crucial tener en cuenta el propósito específico del sistema, ya que puede adaptarse tanto a sensores analógicos como digitales.

En este contexto, se invita a replicar la misma práctica utilizando el micro RP2040, ya que se cuenta con la disponibilidad del conector QWIIC para facilitar la conexión. Se destaca la necesidad de ajustar la configuración del puerto I2C según los pines correspondientes al RP2040.



# Continua con el curso [Comunicación Inalámbrica](/docs/11-comunicacion_inalambrica/)
* [Licencia](https://www.gnu.org/licenses/gpl-3.0.html) El código que se presenta en este repositorio está licenciado bajo la Licencia Pública General de GNU (GPL) versión 3.0.

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊