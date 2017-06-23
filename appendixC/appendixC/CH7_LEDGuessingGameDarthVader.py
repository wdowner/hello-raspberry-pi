# Light Up Guessing Game
# Ryan Heitz
# Guess the number, you get five tries.  A light will light up different
# colors to tell you if your guess is too high, too low, or correct

# importing the libraries we need
import RPi.GPIO as GPIO
import os
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
def flash(LED_pin):
    for i in range(1,6):  #Blink on and off 5 times
        # Turning on LEDs
        GPIO.output(LED_pin, GPIO.HIGH)
        time.sleep(blink_time)
        GPIO.output(LED_pin, GPIO.LOW)
        time.sleep(blink_time)

# An ending to the game if they don't guess it
def game_over():
    print("You lost!")
    print("Better luck next time!")
    time.sleep(2)
    os.system("fim Darth_Vader.jpg")


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

while play_again:
    print(intro)
    # Guessing Game Loop
    while count_guesses < 6:
        guess = input("Guess " + str(count_guesses) + " - What is your guess?: ")
        guess = int(guess)  # Convert the input string to an integer
        count_guesses += 1   # Add one to the number of Guesses to keep track
        if guess == number_in_my_head:  # Guessed it correctly
            flash(LED_pin_green)
            print("You won!  No doom for you!")
            break # Breaks out of loop and skips the else 
        elif guess > number_in_my_head:  # Guess too high
            flash(LED_pin_red)
        elif guess < number_in_my_head:  # Guess too low
            flash(LED_pin_blue)
        else:
            print("You obviously need to study your numbers again!")
    else:
        game_over()
    # End of Guessing Game Loop    
    answer = input("Would you like to play again [Y/N]? ")
    if answer.upper() ==  "Y":
        # Starting over. Get a new random number and reset the guess counter
        number_in_my_head = random.randint(1,20)
        count_guesses = 1
    else:
        play_again = False
print("Good bye!")

GPIO.cleanup()
 
    
