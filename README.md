# SensePi

Real-time sensor dashboard running locally on Raspberry Pi 4. 
A React frontend communicates with a Python FastAPI backend to display 
live DHT11 temperature and humidity data, with a WS2812 RGB LED strip 
controlled from the browser via Arduino.

## Stack
- Frontend: React + Vite
- Backend: Python + FastAPI
- Hardware: Raspberry Pi 4, DHT11 sensor, Arduino R4 Wifi, WS2812 LED strip (15 LEDs)

## Architecture
DHT11 → Raspberry Pi 4 GPIO → Python FastAPI → React UI
WS2812 LED strip → Arduino R4 Wifi → USB Serial → Python FastAPI → React UI

## Hardware connections
### DHT11 → Raspberry Pi 4
- VCC → Pin 1 (3.3V)
- DATA → Pin 7 (GPIO4)
- GND → Pin 9 (GND)

### WS2812 → Arduino R4 Wifi
- VCC → 5V
- DATA → Pin 6
- GND → GND
