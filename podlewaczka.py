import RPi.GPIO as GPIO
import time

# Set the GPIO numbering mode
WATER_POMP = 18 # GPIO 24 - dziala
VALVE_01 = 13 # GPIO 27
LED01 = 12  # GPIO 18 
MOISTURE_SENSOR_PIN = 11  # GPIO17

# Set mode 
GPIO.setmode(GPIO.BOARD)
# Set up each GPIO pin as an output
GPIO.setup(LED01, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(WATER_POMP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(VALVE_01, GPIO.OUT)
GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

# Function to turn both LEDs on or off
def toggle(what, state):
    GPIO.output(what, state)

# Function to blink the LEDs a given number of times
def blink_leds(times):
    for _ in range(times):
        toggle(LED01,GPIO.HIGH)
        time.sleep(0.5)  # On duration
        toggle(LED01,GPIO.LOW)
        time.sleep(0.5)  # Off duration
            
try:
  '''Diode test'''
  blink_leds(2)
  print("Diode test completed")
  while True:
      if GPIO.input(MOISTURE_SENSOR_PIN) == GPIO.LOW:
          print("Sensor detects WET soil 🌱💧")
          GPIO.output(WATER_POMP, GPIO.LOW)
      else:
          print("Sensor detects DRY soil 🌵🔥")
          GPIO.output(WATER_POMP, GPIO.HIGH)
          GPIO.output(VALVE_01, GPIO.LOW)
      time.sleep(1)
  
except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()
GPIO.cleanup()