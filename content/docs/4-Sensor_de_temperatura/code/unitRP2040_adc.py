'''
Unit Electronics 2024
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.1
   revision: 0.0.1
    RP2040 
'''
import machine
import time

# Configura el pin de entrada analógica para leer la salida del LM35

pin_lm35 = machine.Pin(28, machine.Pin.IN)
adc = machine.ADC(pin_lm35)

while True:
   # Lee el valor del sensor LM35 en milivoltios
   lm35_output_mv = adc.read_u16() * 3.3 / 65535  * 1000
   # Convierte el valor a grados Celsius usando la fórmula
   temperatura_celsius = (lm35_output_mv - 500) / 10
   # Imprime la temperatura en grados Celsius
   print("Temperatura: {:.2f} °C".format(temperatura_celsius))
   # Espera un segundo antes de tomar la siguiente lectura

   time.sleep(1)