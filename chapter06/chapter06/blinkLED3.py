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

# Loop to blink our LEDs
while True:
    GPIO.output(LED_pin_red, GPIO.HIGH)
    GPIO.output(LED_pin_green, GPIO.HIGH) 					#C
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    print("On")
    time.sleep(1)
    GPIO.output(LED_pin_red, GPIO.LOW)					
    GPIO.output(LED_pin_green, GPIO.LOW)					#D
    GPIO.output(LED_pin_blue, GPIO.LOW)
    print("Off")
    time.sleep(1)

