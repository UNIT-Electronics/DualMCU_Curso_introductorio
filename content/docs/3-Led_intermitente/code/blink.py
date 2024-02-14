
'''
Unit Electronics 2023
          (o_
   (o_    //\
   (/)_   V_/_ 
   tested code mark
   version: 0.0.1
   revision: 0.0.1
'''
import machine
import time

led_pin = machine.Pin(4, machine.Pin.OUT)
led_pin2 = machine.Pin(26, machine.Pin.OUT)
led_pin3 = machine.Pin(25, machine.Pin.OUT)


def loop():
     while True:
        led_pin.on()    
        led_pin2.on()   
        led_pin3.on()  
        time.sleep(1)  
        led_pin.off()   
        led_pin2.off()  
        led_pin3.off()  
        time.sleep(1)   

loop()
