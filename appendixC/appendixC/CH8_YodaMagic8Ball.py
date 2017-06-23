# Yoda Magic 8 Ball
# Ryan Heitz
# Ask a question then press the button to get an answer from
# the Yoda Magic 8 Ball.  This is styled after the class Magic 8 Ball

# importing the libraries we need
import RPi.GPIO as GPIO
import time
import random
import os

# Variable for the button GPIO input pin
button_pin = 6

play_again = "Y"

#Tell the Pi we want to use a breakout board
GPIO.setmode(GPIO.BCM)

# Setup GPIO pin as input pin (detect electrical signals coming in)
GPIO.setup(button_pin,GPIO.IN)

path_yoda = "/home/pi/yoda/"

# Returns a list of mp3 sound files for the path given
def get_MP3_sounds(sound_path):
    sound_files = os.listdir(sound_path)
    sound_files = [sound_file for sound_file in sound_files
                  if sound_file.endswith('.mp3')]
    return sound_files

# Plays a random sound from a list of mp3s for the path given
def play_random_sound(sound_path, sound_files):
    random_sound_index = random.randint(0,len(sound_files)-1)
    os.system("omxplayer -o local '" + sound_path +
              "/" + sound_files[random_sound_index] + "' >/dev/null")

# Get the list of music loops and vocals (mp3s only)
sounds_yoda = get_MP3_sounds(path_yoda)

# Clear the screen 
os.system("clear")

#Display a title screen
title = """
YODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODAYODA

    Yoda Magic 8 Ball

    Ask it a Yes or No question and press the button
    Yoda will give you an answer

    Press Ctrl + C to exit

MAGIC8BALLMAGIC8BALLMAGIC8BALLMAGIC8BALLMAGIC8BALLMAGIC8BALLMAGIC8BALLMAGIC8BALL
"""
print(title)

print("*" * 80)
print("Ask aloud a Yes or No question, then press the button: ")
print("*" * 80)

# Start an infinite loop (must use Ctrl + C to stop it)
while play_again.upper() == "Y":
    # Check if the button has been pressed
    if GPIO.input(button_pin):
        print("Yoda is considering your question...")
        time.sleep(1)
        print("Listen to Yoda's answer:")
        time.sleep(.5)
        play_random_sound(path_yoda, sounds_yoda)
        # Ask for another question
        print("*" * 80)
        print("Ask aloud a Yes or No question, then press the button: ")
        print("*" * 80)
else:
    print("Thank you for consulting Yoda!")



    
