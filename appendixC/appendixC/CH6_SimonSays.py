# Simon Says
# Ryan Heitz
# Repeat a sequence of colors

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


def simon_says(color1, color2, color3, color4, color5):
    # Create a list with the five colors
    colors = [color1, color2, color3, color4, color5]

    # Loop through the five colors
    for i in range(0,5):
        # Grab the name of a single color and turn on and off the matching LED
        color = colors[i]
        if color == "red":
            GPIO.output(LED_pin_red, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_red, GPIO.LOW)
        elif color == "green":
            GPIO.output(LED_pin_green, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_green, GPIO.LOW)
        elif color == "blue":
            GPIO.output(LED_pin_blue, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_pin_blue, GPIO.LOW)
        time.sleep(1)

# Play the game
print("Ready for #1!")
time.sleep(1)
print("Simon Says: red, green, red, red, blue")
time.sleep(1)
print("Watch my lights!")
time.sleep(1)
simon_says("red", "green", "red", "red", "blue")

print("Ready for #2!")
time.sleep(1)
print("Simon Says: blue, green, blue, green, red")
time.sleep(1)
print("Watch my lights!")
time.sleep(1)
simon_says("blue", "green", "blue", "green", "red")

print("Ready for #3!")
time.sleep(1)
print("Simon Says: green, blue, blue, red, green")
time.sleep(1)
print("Watch my lights!")
time.sleep(1)
simon_says("green", "blue", "blue", "red", "green")
time.sleep(1)
print("Thank you for playing!!!")
