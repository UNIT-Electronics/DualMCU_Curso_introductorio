from machine import Pin, PWM
import time

# Configura los pines para controlar el L298N
l298n_enableA = Pin(7, Pin.OUT)  # Conecta a ENA del L298N
l298n_input1 = Pin(14, Pin.OUT)  # Conecta a IN1 del L298N
l298n_input2 = Pin(9, Pin.OUT)  # Conecta a IN2 del L298N
l298n_enableB = Pin(4, Pin.OUT)  # Conecta a ENB del L298N
l298n_input3 = Pin(8, Pin.OUT)  # Conecta a IN3 del L298N
l298n_input4 = Pin(11, Pin.OUT)  # Conecta a IN4 del L298N

# Habilita el motor
l298n_enableA.on()
l298n_enableB.on()

# Prepara el PWM
pwm1 = PWM(l298n_input1)
pwm1.freq(1000)
pwm2 = PWM(l298n_input2)
pwm2.freq(1000)
pwm3 = PWM(l298n_input3)
pwm3.freq(1000)
pwm4 = PWM(l298n_input4)
pwm4.freq(1000)

# Define la velocidad del motor (ajusta el valor según sea necesario)
motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)
pwm3.duty_u16(motor_speed)
pwm4.duty_u16(0)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(motor_speed)
pwm2.duty_u16(0)
pwm3.duty_u16(motor_speed)
pwm4.duty_u16(0)

time.sleep(2)

motor_speed =  65536 #Velocidad máxima

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)
pwm3.duty_u16(0)
pwm4.duty_u16(motor_speed)

time.sleep(5)

motor_speed =  40000

pwm1.duty_u16(0)
pwm2.duty_u16(motor_speed)
pwm3.duty_u16(0)
pwm4.duty_u16(motor_speed)

time.sleep(2)

l298n_enableA.off()
l298n_enableB.off()