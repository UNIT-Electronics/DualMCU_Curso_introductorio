'''
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.2
   revision: 0.0.2 (2024)
'''

import machine
from ssd1306 import SSD1306_I2C

i2c = machine.SoftI2C(sda=machine.Pin(21), scl=machine.Pin(22))

oled = SSD1306_I2C(128, 32, i2c)

oled.fill(1)
oled.show()

oled.fill(0)
oled.show()
oled.text('UNIT', 50, 10)
oled.text('ELECTRONICS', 25, 20)

oled.show()