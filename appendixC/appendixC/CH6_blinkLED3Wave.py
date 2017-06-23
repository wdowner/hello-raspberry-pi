# Blink 3 LEDs
# Ryan Heitz
# Blinks three LEDs on and off

import RPi.GPIO as GPIO						
import time

# Variable for the GPIO pin number
LED_pin_red = 21								
LED_pin_green = 22								#A
LED_pin_blue = 23								

# Tell the Pi we are using the breakoutboard pin numbering
GPIO.setmode(GPIO.BCM)							

# Setup the GPIO pins for output
GPIO.setup(LED_pin_red, GPIO.OUT)
GPIO.setup(LED_pin_green, GPIO.OUT)						#B
GPIO.setup(LED_pin_blue, GPIO.OUT)

# Loop to blink our LEDs in a wave pattern
while True:
    # Making a wave pattern
    GPIO.output(LED_pin_red, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_pin_green, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_pin_red, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_pin_green, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(1)


