#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# GPIO PINS
WATER_POMP = 12                #GPIO18
def main():
    GPIO.setmode(GPIO.BOARD) # Set the GPIO numbering mode
   
   GPIO.setup(WATER_POMP, GPIO.OUT, initial=GPIO.LOW) # Set water pomp to close
    time.sleep(2)
    GPIO.output(WATER_POMP, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(WATER_POMP, GPIO.LOW)
    time.sleep(2)
    GPIO.output(WATER_POMP, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(WATER_POMP, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
  main()
