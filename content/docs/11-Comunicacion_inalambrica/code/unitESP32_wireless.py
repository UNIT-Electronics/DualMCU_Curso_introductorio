import network
import ubinascii
import machine
import urequests
import time
import _thread

try:
  import usocket as socket
except:
  import socket
  
ssid = "SSID"  # Reemplaza con el nombre de tu red Wi-Fi
password = "PASSWORD"  # Reemplaza con la contraseña de tu red Wi-Fi

server_url = "http://tu_host:3000/endpoint" # Reemplaza con el nombre de la ip de tu servidor
headers = {"Content-Type": "application/json"}

led = machine.Pin(25, machine.Pin.OUT)
#led_pin2 = machine.Pin(26, machine.Pin.OUT)
shared_variable = 0

# Convierte la dirección MAC del ESP32 en un nombre de host único
def generate_unique_hostname():
    mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    return "esp32-" + mac

# Conecta a la red Wi-Fi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Conectando a la red WiFi...")
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Conectado a la red WiFi")
    print("Dirección IP:", wlan.ifconfig()[0])
    
def adc_potenciometer():
    
    potentiometer_pin = machine.Pin(36)
    adc = machine.ADC(potentiometer_pin)
    adc.atten(machine.ADC.ATTN_11DB)
    return adc


def web_page(adc1):
    led_state = 0
    html = """<html>

    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            html {
                font-family: Arial;
                display: inline-block;
                margin: 0px auto;
                text-align: center;
            }

            .button {
                background-color: #F146C2;
                border: none;
                color: white;
                padding: 16px 40px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }

            .button1 {
                background-color: #304169;
            }
        </style>
    </head>

    <body>
        <h2>Soy el ESP32</h2>
        <p>
            <a href=\"?led_2_on\"><button class="button">LED ON</button></a>
        </p>
        <p>
            <a href=\"?led_2_off\"><button class="button button1">LED OFF</button></a>
        </p>
    </body>

    </html>"""
    return html

def loop1():
    global shared_variable
    while True: 
        adc1=adc.read()/4096*100
        data = {"potentiometer_value": str(adc1)} 
        response = urequests.post(server_url, json=data, headers=headers)
        response.close() 
        time.sleep(0.1)  
    
def loop2():
    global shared_variable
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 80))
    s.listen(5)
     
    while True:
      try:
        if gc.mem_free() < 102000:
          gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        if led_on == 6:
            led_state = "ON"
            led.on()
        if led_off == 6:
            led_state = "OFF"
            led.off()
        response = web_page(shared_variable)
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
      except OSError as e:
        conn.close()
        print('Connection closed')
      
    
    
connect_to_wifi()
adc = adc_potenciometer()

# Crear y lanzar los hilos
_thread.start_new_thread(loop1, ())
_thread.start_new_thread(loop2, ())

time.sleep(10)
