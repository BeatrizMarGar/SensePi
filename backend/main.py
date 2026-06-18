from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import adafruit_dht #librería para el sensor
import board #define los pines de la raspby
from rpi_ws281x import PixelStrip, Color

app = FastAPI()

#CORS para que React hable con FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#SENSOR
sensor = adafruit_dht.DHT11(board.D4)

#config TIRA LED
LED_COUNT = 15
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50
LED_INVERT = False
LED_CHANNEL = 0

#Conexión de la tira con el hardware
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                   LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

#empezamos por defecto en apagado
led_state = {"r": 0, "g": 0, "b": 0, "encendido": False}

#-----
# ENDPOINTS

@app.get("/sensor")
def get_sensor():
	try:
		temperatura = sensor.temperature
		humedad = sensor.humidity
		return {
			"temperatura": temperatura,
			"humedad": humedad,
			"estado": "ok"
		}
	except RuntimeError as e: 
		return {
            		"temperatura": None,
            		"humedad": None,
            		"estado": f"error: {str(e)}"
        	}

@app.get("/led")
def get_led():
    	return led_state

@app.post("/led")
def set_led(data: dict):
    r = data.get("r", 0)
    g = data.get("g", 0)
    b = data.get("b", 0)
    encendido = data.get("encendido", False)

    if encendido:
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(r, g, b))
    else:
        for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(0, 0, 0))

    strip.show()
    led_state.update({"r": r, "g": g, "b": b, "encendido": encendido})
    return led_state
