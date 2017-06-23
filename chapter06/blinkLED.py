# Blink LED
# Ryan Heitz
# Blinks an LED on and off

import RPi.GPIO as GPIO
import time

# Variable for the GPIO pin number
LED_pin_red = 21

# Tell the Pi we are using the breakoutboard pin numbering
GPIO.setmode(GPIO.BCM)							

# Setup the GPIO pin for output
GPIO.setup(LED_pin_red, GPIO.OUT)

# Loop to blink our led
while True:
    GPIO.output(LED_pin_red, GPIO.HIGH)
    print("On")
    time.sleep(1)
    GPIO.output(LED_pin_red, GPIO.LOW)
    print("Off")
    time.sleep(1)
