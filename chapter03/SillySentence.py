# Title: The Silly Sentence Generator 3000
# Author: Ryan Heitz
# This is an interactive game that creates funny sentences
# based on input from the user

# Display a welcome message
print("*" * 48)
print("* Welcome to the Silly Sentence Generator 3000 *")
print("*" * 48)

# Get the user's name and say hi
player_name = input("Please enter your name: ")
message = "Hello, " + player_name + "!  Let's make a silly sentence!"
print(message)

# Gather words from the player for our sentences
famous_person = input("Enter the name of a famous person: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb = input("Enter a verb ending in -ING: ")

#Create the sentence by joining together the words
silly_sentence = ("The " + adjective1 + " " + player_name + " is " +
                 verb + " the " + adjective2 + " " + famous_person)

#Display the silly sentence to the screen
print("*" * len(silly_sentence))
print(silly_sentence)
print("*" * len(silly_sentence))
