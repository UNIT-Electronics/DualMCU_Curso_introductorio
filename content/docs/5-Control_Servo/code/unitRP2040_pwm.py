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
import utime

# Configuración del pin PWM
pwm_pin = machine.Pin(0)  # Cambia a machine.Pin(1) si estás usando el pin GPIO 1
pwm = machine.PWM(pwm_pin)

# Frecuencia del PWM en Hz (ajusta según tus necesidades)
pwm.freq(1000)

try:
    while True:
        # Ciclo de trabajo del PWM (0-65535, donde 0 es apagado y 65535 es encendido)
        for duty_cycle in range(0, 65536, 5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

        # Invierte el ciclo de trabajo para un efecto de atenuación
        for duty_cycle in range(65535, -1, -5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

except KeyboardInterrupt:
    # Detén el PWM y limpia los recursos al interrumpir el programa con Ctrl+C
    pwm.deinit()
    print("\nPWM detenido. Recursos liberados.")
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
import utime

# Configuración del pin PWM
pwm_pin = machine.Pin(0)  # Cambia a machine.Pin(1) si estás usando el pin GPIO 1
pwm = machine.PWM(pwm_pin)

# Frecuencia del PWM en Hz (ajusta según tus necesidades)
pwm.freq(1000)

try:
    while True:
        # Ciclo de trabajo del PWM (0-65535, donde 0 es apagado y 65535 es encendido)
        for duty_cycle in range(0, 65536, 5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

        # Invierte el ciclo de trabajo para un efecto de atenuación
        for duty_cycle in range(65535, -1, -5000):
            pwm.duty_u16(duty_cycle)
            utime.sleep(0.1)

except KeyboardInterrupt:
    # Detén el PWM y limpia los recursos al interrumpir el programa con Ctrl+C
    pwm.deinit()
    print("\nPWM detenido. Recursos liberados.")
