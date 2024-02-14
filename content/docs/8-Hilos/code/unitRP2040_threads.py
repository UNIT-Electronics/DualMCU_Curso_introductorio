'''
Unit Electronics 2023
        >o)
        (_>
file: share_data.py
author: Cesar
version: 0.0.1
revision: 0.0.1
context: This code facilitates the sharing of data within a counter through the utilization of threads.

ESP32
'''
import _thread
import time

shared_variable = 0

def increment_thread():
    global shared_variable
    for _ in range(10):
        shared_variable += 1
        time.sleep(1)

def print_thread():
    global shared_variable
    for _ in range(10):
        print("Valor compartido:", shared_variable)
        time.sleep(1)

# Crear y lanzar los hilos
_thread.start_new_thread(increment_thread, ())
_thread.start_new_thread(print_thread, ())

time.sleep(10)