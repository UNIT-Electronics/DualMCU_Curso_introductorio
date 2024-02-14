'''
Unit Electronics 2024
       (o_
(o_    //\
(/)_   V_/_ 

version: 0.0.1
revision: 0.0.1
compiler: MicroPython v1.22.0 on 2023-12-27; Generic ESP32 module with ESP32
'''
from dht import DHT11
from machine import Pin, ADC
from time import sleep

sensor = DHT11 (Pin(4))

# configura entrada de adc en el pin 36

adc = ADC(Pin(36))
# configura el rango de lectura de 0 a 3.3v
adc.atten(ADC.ATTN_11DB)
# configura el rango de lectura de 0 a 4095
adc.width(ADC.WIDTH_12BIT)

while True:
  try:
    sleep(2)
    valor = adc.read()
    #imprime el valor del adc
    print(valor)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')