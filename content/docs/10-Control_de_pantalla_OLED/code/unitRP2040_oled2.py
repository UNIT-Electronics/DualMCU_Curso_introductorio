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
