import time
from rpi_ws281x import PixelStrip, Color

# Configuración de la tira
LED_COUNT = 15
LED_PIN = 18        # GPIO18 = Pin físico 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50  # 0-255, bajo para no deslumbrar
LED_INVERT = False
LED_CHANNEL = 0

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

print("Probando rojo...")
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(255, 0, 0))
strip.show()
time.sleep(2)

print("Probando verde...")
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0, 255, 0))
strip.show()
time.sleep(2)

print("Probando azul...")
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0, 0, 255))
strip.show()
time.sleep(2)

print("Apagando...")
for i in range(LED_COUNT):
    strip.setPixelColor(i, Color(0, 0, 0))
strip.show()

print("Test completado")
