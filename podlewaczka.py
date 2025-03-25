import RPi.GPIO as GPIO
import time

WATER_POMP = 16 # GPIO 23
VALVE_01 = 18 # GPIO 24
MOISTURE_SENSOR_01 = 11  # GPIO17
MOISTURE_SENSOR_02 = 13 #GPIO22
# Set the GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set up each GPIO pin
GPIO.setup(WATER_POMP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(VALVE_01, GPIO.OUT)
GPIO.setup(MOISTURE_SENSOR_01, GPIO.IN)
GPIO.setup(MOISTURE_SENSOR_02, GPIO.IN)

           
try:
  while True:
      if GPIO.input(MOISTURE_SENSOR_01) == GPIO.LOW:
          #GPIO.output(WATER_POMP, GPIO.LOW)
          print("Sensor 01 detects WET soil 🌱💧")
          print("Water pomp start")
      else:
          print("Sensor 01 detects DRY soil 🌵🔥")
          #GPIO.output(WATER_POMP, GPIO.HIGH)
          print("Water pomp stop")
          #GPIO.output(VALVE_01, GPIO.LOW)
          print("Valve 01 action")
      if GPIO.input(MOISTURE_SENSOR_02) == GPIO.LOW:
          print("Sensor 02 detects WET soil 🌱💧")
          #GPIO.output(WATER_POMP, GPIO.LOW)
          print("Water pomp start")
      else:
          print("Sensor 02 detects DRY soil 🌵🔥")
          #GPIO.output(VALVE_01, GPIO.LOW)
          print("Valve 01 action")
          #GPIO.output(WATER_POMP, GPIO.HIGH)
          print("Water pomp stop")
      time.sleep(2)
      print("Soil wet on all plants")
except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()
GPIO.cleanup()