# Random Blinking
# Ryan Heitz
# Blink LEDs in a random pattern

import RPi.GPIO as GPIO						
import random
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

# Loop to blink our LED
while True:
    # Get a random number
    on_random_time = random.random() * 3
    off_random_time = random.random() * 3

    # Turn the lights on for a random amount of time
    GPIO.output(LED_pin_red, GPIO.HIGH)
    GPIO.output(LED_pin_green, GPIO.HIGH)
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(on_random_time)

    # Turn the lights off for a random amount of time
    GPIO.output(LED_pin_red, GPIO.LOW)
    GPIO.output(LED_pin_green, GPIO.LOW)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(off_random_time)
    
    
