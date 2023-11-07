---
title: 2. Características 
type: docs
weight: 2
BookToC: false
---

# Características de la DualMCU

## 2. Características

**Vista frontal** ![Block_Diagram](/docs/2-Caracteísticas/images/Front_View_DualMCU_Topology.jpg "Block Diagram")

| Ref. | Descripción | Ref. | Descripción
|----------|----------|----------|-------|
|  U1  | Microcontrolador Raspberry Pi RP2040   |   U4  | Circuito integrado de conversión USB CH340C |
|  U2  | Módulo Wi-Fi/Bluetooth® Espressif ESP32 WROOM    |   U5  | Circuito integrado de gestión de carga de batería MCP73831 |
|  U3  | Circuito integrado de memoria flash de 2 MB W25Q16JVUXIQ  |   U6  | Regulador de voltaje LDO 3.3V AP2112K |
|  L1  | LED de encendido   |   L2  | LED de carga |
|  L3  | LED (GPIO25)   |   L4  | WS2812B LED |
|  L5  | LED RGB 2020  |   J1  | Conector USB tipo C macho |
|  PB1  | Botón de reinicio RP2040   |   PB2  |  Botón de arranque RP2040 |
|  PB3  | Botón de flasheo ESP32     |   PB4  | Botón de reinicio ESP32 |
|  JP1  |GPIO Pines de la RP2040    |   JP2  | ESP32 GPIO Header |
|  JP3  |RP2040 (SWD) Debug Header    |   JST1  | Conector JST I2C RP2040  |
|  JST2  | Conector JST I2C ESP32  |   JST3  | Conector JST para batería de litio (LiPo) |
|  SW2  | Selector de comunicación USB   |   SW3  | Interruptor DIP UART |

**Vista reverso**

![Block_Diagram](/docs/2-Caracteísticas/images/Back_View_DualMCU_Topology.jpg "Block Diagram")

| Ref. | Description | Ref. | Description
|----------|----------|----------|-------|
|  U7  | Soporte para el circuito integrado criptográfico ATECC608A-MAHDA-T   |   J2  |  Conector para tarjeta microSD |
|  SW1  | Interruptor de encendido   |   SB1  | Puente de soldadura del LED de carga (desconectado por defecto) |
|  SB2  | Puente de soldadura del sensor VBUS (desconectado por defecto) |   SB3  | Regulador de voltaje LDO 3.3V AP2112K |
|  SB4  | uente de soldadura del reinicio ESP32 (desconectado por defecto)   |   SB5  |  Puente de soldadura del selector de señal SCL para ATECC608A-MAHDA-T (desconectado por defecto)|
|  SB6  | Puente de soldadura del selector de señal SDA para ATECC608A-MAHDA-T (desconectado por defecto)|   B1  |Pads de soldadura para batería de litio (LiPo) |