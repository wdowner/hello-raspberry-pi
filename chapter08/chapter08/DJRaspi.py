# DJ Raspi
# Ryan Heitz
# Press push buttons to play different sounds

# importing the libraries we need
import RPi.GPIO as GPIO
import time
import random
import os

# Variables for the button GPIO input pins
button_pin1 = 6
button_pin2 = 19

#Tell the Pi we want to use a breakout board
GPIO.setmode(GPIO.BCM)

# Setup GPIO pins as input pins (detect electrical signals coming in)
GPIO.setup(button_pin1,GPIO.IN)
GPIO.setup(button_pin2,GPIO.IN)

path_music = "/usr/share/scratch/Media/Sounds/Music Loops/"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals/"

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
              "/" + sound_files[random_sound_index] + "' &")

# Get the list of music loops and vocals (mp3s only)
sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)

# Clear the screen 
os.system("clear")

#Display a title screen
title = """
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

    DJ RASPI

    Press Button 1 for Music Sounds
    Press Button 2 for Electronic Sounds

    Press Ctrl + C to exit

JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
"""
print(title)

# Start an infinite loop (must use Ctrl + C to stop it)
while True:
    if GPIO.input(button_pin1):
        #print("You pressed #1!")
        play_random_sound(path_music, sounds_music)
        time.sleep(.1)
    if GPIO.input(button_pin2):
        #print("You pressed #2!")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(.1)
    time.sleep(.1)



    
