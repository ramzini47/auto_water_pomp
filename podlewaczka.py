#!/usr/bin/python3.9
import RPi.GPIO as GPIO
import time
import logging

# Configure logging
logging.basicConfig(
    filename='/home/pi/repo/auto_water_pomp/watering.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
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
  GPIO.setup(v_pin, GPIO.OUT)
for s_name, s_pin in MOISTURE_SENSORS.items():
  GPIO.setup(s_pin, GPIO.IN)

def water_the_plant(sensor_name, sensor_pin):           
  print(f"{sensor_name} detects DRY soil. Start punmping!!!")
  logging.info(f"{sensor_name} detects DRY soil. Start punmping!!!")
  if sensor_name == 'MOISTURE_SENSOR_02':
      valve_name = 'VALVE_01'
      valve_pin = VALVES[valve_name]
      GPIO.output(valve_pin, GPIO.HIGH)  # Open the valve
      print(f"{valve_name} opened.")
      logging.info(f"{valve_name} opened.")
  GPIO.output(WATER_POMP, GPIO.HIGH)
  while GPIO.input(sensor_pin) == GPIO.HIGH:
    time.sleep(1)
  GPIO.output(WATER_POMP, GPIO.LOW)
  if sensor_name == 'MOISTURE_SENSOR_02':
      GPIO.output(valve_pin, GPIO.LOW)  # Close the valve
      print(f"{valve_name} closed.")
      logging.info(f"{valve_name} closed.")
  print(f"{sensor_name} detects WET soil. Stopt punmping!!!")
  logging.info(f"{sensor_name} detects WET soil. Stopt punmping!!!")

def main():
  try:
    for sensor_name, sensor_pin in MOISTURE_SENSORS.items():
      if GPIO.input(sensor_pin) == GPIO.HIGH:
        water_the_plant(sensor_name, sensor_pin)
      else:
        print(f"{sensor_name} detects WET soil. No water needed")
        logging.info(f"{sensor_name} detects WET soil. No water needed")
  except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()
  except Exception as e:
      logging.error("An error occurred: %s", e)
  finally:
    GPIO.cleanup()
    
if __name__ == "__main__":
  main()