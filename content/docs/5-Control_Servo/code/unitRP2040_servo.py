import machine
import utime

# Configuración del pin de control del servomotor (puedes cambiarlo según tus conexiones)
servo_pin = machine.Pin(0)  # Cambia a tu pin deseado

# Crea un objeto PWM para controlar el servomotor
pwm_servo = machine.PWM(servo_pin)

# Frecuencia del PWM para el servomotor (generalmente alrededor de 50 Hz)
pwm_servo.freq(50)

def set_servo_angle(angle):
    # Convierte el ángulo deseado (en grados) a un valor de ciclo de trabajo
    # Ten en cuenta que los valores específicos pueden variar según el servo
    duty_cycle = int(1024 + (angle / 180) * 3072)
    pwm_servo.duty_u16(duty_cycle)

try:
    while True:
        # Mueve el servomotor de 0 a 180 grados
        for angle in range(0, 181, 10):
            set_servo_angle(angle)
            utime.sleep(0.1)

        # Mueve el servomotor de 180 a 0 grados
        for angle in range(180, -1, -10):
            set_servo_angle(angle)
            utime.sleep(0.1)

except KeyboardInterrupt:
    # Detén el PWM y limpia los recursos al interrumpir el programa con Ctrl+C
    pwm_servo.deinit()
    print("\nPWM detenido. Recursos liberados.")