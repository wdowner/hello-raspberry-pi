# Light Up guessing Game
# Ryan Heitz
# guess the number, you get five tries.  A light will light up different
# colors to tell you if your guess is too high, too low, or correct

# importing the libraries we need
import RPi.GPIO as GPIO
import time
import random

#Tell the Pi we want to use a breakout board
GPIO.setmode(GPIO.BCM)

# Create variables for the pins used for LEDs
LED_pin_red = 12 
LED_pin_green = 16
LED_pin_blue = 21

# Blink speed in seconds
blink_time = 0.25

# Tell the Pi which Pins we will use
# Set them up as OUT pins (send electricity out)
GPIO.setup(LED_pin_red,GPIO.OUT)
GPIO.setup(LED_pin_green,GPIO.OUT)
GPIO.setup(LED_pin_blue,GPIO.OUT)

# Blinks an LED.  
def flash(LEDPin):
    for i in range(1,6):  #Blink on and off 5 times
        # Turning on LEDs
        GPIO.output(LEDPin, GPIO.HIGH)
        time.sleep(blink_time)
        GPIO.output(LEDPin, GPIO.LOW)
        time.sleep(blink_time)

# An ending to the game if they don't guess it
def game_over():
    print("You lost!")
    print("Better luck next time!")
    time.sleep(2) 

# Function to create a winning flash sequence
def winning_flash():
    # flash three different colors ten times
    for i in range(0,20):
        # flash the Red LED
        GPIO.output(LED_pin_red, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_pin_red, GPIO.LOW)
        time.sleep(0.05)

        # flash the Green LED
        GPIO.output(LED_pin_green, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_pin_green, GPIO.LOW)
        time.sleep(0.05)

        # flash the Blue LED
        GPIO.output(LED_pin_blue, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(LED_pin_blue, GPIO.LOW)
        time.sleep(0.05)

# A random number for our game
number_in_my_head = random.randint(1,20)
count_guesses = 1  # Counter for the number of guesses

# Used to keep track of whether they want to play again
play_again = True

title = """
********************************************************************************
                              Light Up Guessing Game
********************************************************************************
"""
print(title)

intro = """
Game Play:
I'm thinking of a number between 1 and 20. You have five guesses to guess it.
After each guess, my light will blink.

  Red ---> Your guess is too high!
  Green ---> Your guess is correct!
  Blue --> Your guess is too low
"""

print(intro)

# guessing Game Loop
while count_guesses < 6:
    guess = input("What is your guess?: ")
    guess = int(guess)  # Convert the input string to an integer
    count_guesses += 1   # Add one to the number of guesses to keep track
    if guess == number_in_my_head:  # guessed it correctly
        flash(LED_pin_green)
        print("You won!  No doom for you!")
        time.sleep(1)
        winning_flash()
        time.sleep(1)
        break # Breaks out of loop and skips the else 
    elif guess > number_in_my_head:  # guess too high
        flash(LED_pin_red)
    elif guess < number_in_my_head:  # guess too low
        flash(LED_pin_blue)
    else:
        print("You obviously need to study your numbers again!")
else:
    game_over()

GPIO.cleanup()
 
    
