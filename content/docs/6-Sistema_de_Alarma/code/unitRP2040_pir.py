
from machine import Pin
import time

# Configura el pin del sensor PIR y el buzzer
pir_pin = Pin(16, Pin.IN)  # Reemplaza el número de pin según tu conexión
buzzer_pin = Pin(15, Pin.OUT)  # Reemplaza el número de pin según tu conexión


# Función para activar la alarma
def activate_alarm():
    print("¡Movimiento detectado! Activando alarma...")
    buzzer_pin.on()
    time.sleep(5)  # La alarma suena durante 5 segundos
    buzzer_pin.off()

print("Sistema de alarma PIR activado")

while True:
    if pir_pin.value() == 1:  # El sensor PIR detecta movimiento
        activate_alarm()
    
    time.sleep(0.5)  # Espera 0.5 segundos antes de volver a verificar el sensor PIR
