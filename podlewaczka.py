import RPi.GPIO as GPIO
import time
# GPIO PINS
WATER_POMP = 16                #GPIO23
VALVES = {
  'VALVE_01': 18               #GPIO24
}
MOISTURE_SENSORS = {
  'MOISTURE_SENSOR_01': 11,    #GPIO17
  'MOISTURE_SENSOR_02': 13     #GPIO22
}
# Set the GPIO numbering mode
GPIO.setmode(GPIO.BOARD)
# Set up each GPIO pin
GPIO.setup(WATER_POMP, GPIO.OUT, initial=GPIO.LOW) #So water pump will not start byitsefl
for v_name, v_pin in VALVES.items():
  GPIO.setup(v_name, GPIO.OUT)
for s_name, s_pin in MOISTURE_SENSORS.items():
  GPIO.setup(s_name, GPIO.IN)

def water_the_plant(sensor_name, sensor_pin):           
  print(f"{sensor_name} detects DRY soil. Start punmping!!!")
  if sensor_name == 'MOISTURE_SENSOR_02':
      valve_name = 'VALVE_01'
      valve_pin = VALVES[valve_name]
      GPIO.output(valve_pin, GPIO.HIGH)  # Open the valve
      print(f"{valve_name} opened.")
  #GPIO.output(WATER_POMP, GPIO.HIGH)
  while GPIO.input(sensor_pin) == GPIO.HIGH:
    time.sleep(1)
  #GPIO.output(WATER_POMP, GPIO.LOW)
  if sensor_name == 'MOISTURE_SENSOR_02':
      GPIO.output(valve_pin, GPIO.LOW)  # Close the valve
      print(f"{valve_name} closed.")
  print(f"{sensor_name} detects WET soil. Stopt punmping!!!")
  
try:
  while True:
    for sensor_name, sensor_pin in MOISTURE_SENSORS.items():
      if GPIO.input(sensor_pin) == GPIO.HIGH:
        water_the_plant(sensor_name, sensor_pin)
      else:
        print(f"{sensor_name} detects WET soil. No water needed")
    time.sleep(10)
except KeyboardInterrupt:
  print("Stopping...")
  GPIO.cleanup()
finally:
  GPIO.cleanup()