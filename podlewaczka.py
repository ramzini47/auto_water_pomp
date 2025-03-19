import RPi.GPIO as GPIO
import time


# Set the GPIO numbering mode
WATER_POMP = 18 # GPIO 24 - dziala
VALVE_01 = 16 # 23
LED1 = 12  # GPIO 18 - dziala
LED2 = 16  # GPIO 23 - cos nie dizala, robie 16 zeby sprawdzac jak zawor dziala
MOISTURE_SENSOR_PIN = 16  # Physical Pin 11 (GPIO17)

# Set mode 
GPIO.setmode(GPIO.BOARD)
# Set up each GPIO pin as an output
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(WATER_POMP, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(VALVE_01, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOISTURE_SENSOR_PIN, GPIO.IN)

# Function to turn both LEDs on or off
def toggle(what, state):
    GPIO.output(what, state)

# Function to blink the LEDs a given number of times
def blink_leds(times):
    for _ in range(times):
        toggle(LED1,GPIO.HIGH)
        time.sleep(0.5)  # On duration
        toggle(LED1,GPIO.LOW)
        time.sleep(0.5)  # Off duration

    
'''
try:
    while True:
        if GPIO.input(MOISTURE_SENSOR_PIN) == GPIO.LOW:
            print("Sensor detects WET soil 🌱💧")
        else:
            print("Sensor detects DRY soil 🌵🔥")
        time.sleep(1)
'''
try:
  blink_leds(2)
  
except KeyboardInterrupt:
    print("Stopping...")
    GPIO.cleanup()