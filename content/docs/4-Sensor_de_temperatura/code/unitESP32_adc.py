'''
Unit Electronics 2024
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
ESP32
'''

import machine
import time
# configura entrada de adc en el pin 36
adc = machine.ADC(machine.Pin(36))
# configura el rango de lectura de 0 a 3.3v
adc.atten(machine.ADC.ATTN_11DB)
# configura el rango de lectura de 0 a 4095
adc.width(machine.ADC.WIDTH_12BIT)
# configura el pin 2 como salida
led = machine.Pin(2, machine.Pin.OUT)
# configura el pin 25 como salida
led2 = machine.Pin(25, machine.Pin.OUT)
#Comienza el ciclo infinito

while True:
   #lee el valor del adc
   valor = adc.read()
   #imprime el valor del adc
   print(valor)
   #si el valor es mayor a 2000 enciende el led
   if valor > 2000:
       led.value(1)
       led2.value(0)
   #si el valor es menor a 2000 enciende el led
   else:
       led.value(0)
       led2.value(1)               
   #espera 1 segundo       
   time.sleep(1)