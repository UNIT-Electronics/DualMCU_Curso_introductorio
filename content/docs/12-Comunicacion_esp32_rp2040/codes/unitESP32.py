'''
ESP32
'''
import ujson
from machine import UART, Pin

uart0 = UART(1, baudrate=115000, tx=Pin(17, Pin.OUT), rx=Pin(16, Pin.IN))
led_rojo = Pin(4, Pin.OUT)  # Configura el pin GPIO5 como salida para el LED rojo
led_verde = Pin(26, Pin.OUT)  # Configura el pin GPIO18 como salida para el LED verde
led_azul = Pin(25, Pin.OUT)  # Configura el pin GPIO19 como salida para el LED azul

def ejecutar_accion(accion, pin_led):
    if accion == "encender":
        pin_led.on()  # Enciende el LED
    elif accion == "apagar":
        pin_led.off()  # Apaga el LED

def recibir_json():
    rx_data = b''  # Inicializa una cadena de bytes vacía

    while True:
        if uart0.any():
            byte_received = uart0.read(1)  # Lee un byte desde el UART
            rx_data += byte_received

            # Verifica si el carácter de nueva línea indica el final del JSON
            if byte_received == b'\n':
                try:
                    # Intenta cargar el JSON
                    json_data = ujson.loads(rx_data.decode('utf-8'))
                    print("JSON recibido:", json_data)
                    
                    # Extrae los valores de 'accion' y 'led_actual' del JSON
                    accion = json_data.get('accion', '')
                    led_actual = json_data.get('led_actual', '')

                    # Ejecuta la acción indicada en el JSON para cada LED
                    if led_actual == "rojo":
                        ejecutar_accion(accion, led_rojo)
                    elif led_actual == "verde":
                        ejecutar_accion(accion, led_verde)
                    elif led_actual == "azul":
                        ejecutar_accion(accion, led_azul)
                    print("--led recibido:", led_actual, "accion:", accion)
                    
                    return json_data
                except ValueError as e:
                    print("Error al parsear JSON:", e)
                    rx_data = b''  # Reinicia la cadena si hay un error en el JSON

# Ejemplo de uso
while True:
    data = recibir_json()
    # Realiza acciones con el JSON recibido
