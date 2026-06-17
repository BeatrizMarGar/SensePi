from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

led_state = {"encendido": False}

@app.get("/sensor")
def get_sensor():
	return {
		"temperatura": round(random.uniform(20.0, 25.0), 1),
		"humedad": round(random.uniform(40.0, 60.0), 1),
		"estado": "ok"
	}

@app.get("/led")
def get_led():
	return led_state

@app.post("/led")
def set_led(data: dict):
	led_state["encendido"] = data.get("encendido", False)
	return led_state
