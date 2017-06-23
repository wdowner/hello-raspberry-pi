# Rock, Paper, Scissors!
# Ryan Heitz
# A game where you play the classic game Rock, Paper, Scissors!

import random

play_again = "Yes"
choices = ["Rock","Paper","Scissors"]

title = "Rock, Paper, Scissors!"
print("*" * 80)
print(title)
print("*" * 80)

while play_again == "Yes":
    print("Choose Rock, Paper, or Scissors:")

    # Get the player's choice
    player_choice = input("Enter your choice: ")

    # Get a random computer choice
    computer_choice = choices[random.randint(0,2)]

    # Display the two choices
    print("You choice is " + player_choice + ".")
    print("The computer's choice is " + computer_choice + ".")
    if player_choice == computer_choice:
        print("It's a tie")
    else:
        if ((player_choice == "Rock" and computer_choice == "Scissors") or 
        (player_choice == "Scissors" and computer_choice == "Paper") or 
        (player_choice == "Paper" and computer_choice == "Rock")):
            print("!" * 80)
            print("You win!")
            print("!" * 80)
        else:
            print(":(" * 40)
            print("You lose!")
            print(":(" * 40)
    play_again = input("Do you want to play again [Yes/No]? ")

print("Thank you for playing!")
     
