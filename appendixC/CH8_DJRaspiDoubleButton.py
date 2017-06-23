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

path_music = "/usr/share/scratch/Media/sounds/_music Loops/"
path_vocals = "/usr/share/scratch/Media/sounds/_vocals/"
path_effects = "/usr/share/scratch/Media/sounds/_effects/"

# Returns a list of mp3 sound files for the path given
def get_MP3_sounds(sound_path):
    sound_files = os.listdir(sound_path)
    sound_files = [SoundFile for SoundFile in sound_files
                  if SoundFile.endswith('.mp3')]
    return sound_files

# Plays a random sound from a list of mp3s for the path given
def play_random_sound(sound_path, sound_files):
    RandomSoundIndex = random.randint(0,len(sound_files)-1)
    os.system("omxplayer -o local '" + sound_path +
              "/" + sound_files[RandomSoundIndex] + "' &")

# Get the list of _music loops and _vocals (mp3s only)
sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects = get_MP3_sounds(path_effects)

# Clear the screen 
os.system("clear")

#Display a title screen
title = """
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

    DJ RASPI

    Press Button 1 for _music sounds
    Press Button 2 for Electronic sounds

    Press Ctrl + C to exit

JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ
"""
print(title)

# Start an infinite loop (must use Ctrl + C to stop it)
while True:
    if GPIO.input(button_pin1) & GPIO.input(button_pin2):
        #print("You pressed both #1 and #2!")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(.1)
    elif GPIO.input(button_pin1):
        #print("You pressed #1!")
        play_random_sound(path_music, sounds_music)
        time.sleep(.1)
    elif GPIO.input(button_pin2):
        #print("You pressed #2!")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(.1)
    
    time.sleep(.1)



    
