from machine import Pin
import time

# Configura los pines para controlar el L298N
l298n_enable = Pin(7, Pin.OUT)  # Conecta a EN del L298N
l298n_input1 = Pin(14, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(9, Pin.OUT)  # Conecta a IN2 del L298N

# Habilita el motor
l298n_enable.on()
# Control del motor
l298n_input1.on()
l298n_input2.off()

#Espera 5s
time.sleep(5)
#Deshabilita el motor
l298n_enable.off()

#Espera 1s
time.sleep(1)
#Habilita el motor
l298n_enable.on()
# Control del motor, sentido contrario
l298n_input1.off()  
l298n_input2.on()  

#Espera 5s
time.sleep(5)
l298n_enable.off()
