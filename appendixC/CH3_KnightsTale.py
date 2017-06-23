
title = "Knight's Tale Creator 3000"
print("*" * 80)
print(title)
print("*" * 80)

# Gather input from the player
player_name = input("Enter your name: ")
adjective = input("Enter an adjective: ")
famous_person = input("Enter the name of a famous person: ")
animal = input("Enter the name of an animal: ")
vacation_place = input("Enter a place you would go on vacation: ")
sharp_thing = input("Enter the name of something sharp: ")
cxclamation = input("Enter something you might exclaim aloud: ")

# Create the sentences by joining the input words
sentence1 = "There was a brave knight, " + player_name + ", who was sent on a quest to vanquish the " + adjective + " evildoer, " + famous_person + ". "  
sentence2 = "Riding on his/her trusty " + animal + ", the brave " + player_name + " traveled to the faraway land of " + vacationPlace + ". "  
sentence3 = player_name + " battled valiantly against " + famous_person + "’s army using his " + sharp_thing + " until he defeated them. "
sentence4 = "Emerging victorious, " + player_name + " exclaimed, '" + exclamation + "!!!' I claim the land of " + vacation_place + " in the name of Python."

# Join together the sentences and display it to the screen
tale = sentence1 + sentence2 + sentence3 + sentence4
print(tale)
