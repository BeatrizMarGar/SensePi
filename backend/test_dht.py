import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT11(board.D4)

print("Leyendo sensor DHT11...")

for i in range(5):
    try:
        temperatura = sensor.temperature
        humedad = sensor.humidity
        print(f"Temperatura: {temperatura}°C  Humedad: {humedad}%")
    except RuntimeError as e:
        print(f"Error de lectura (normal en DHT11): {e}")
    time.sleep(2)

sensor.exit()
print("Test completado")
