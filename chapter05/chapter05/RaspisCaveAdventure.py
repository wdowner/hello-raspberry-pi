# Raspi's Cave Adventure
# Ryan Heitz
# A cave adventure game where you can choose your path through a
# series of caves

import time
def title():
    print("""
__________                       .__/\                           
\______   \_____    ____________ |__)/______                     
 |       _/\__  \  /  ___/\____ \|  |/  ___/                     
 |    |   \ / __ \_\___ \ |  |_> >  |\___ \                      
 |____|_  /(____  /____  >|   __/|__/____  >                     
        \/      \/     \/ |__|           \/                      
_________                                                        
\_   ___ \_____ ___  __ ____                                     
/    \  \/\__  \\  \/ // __ \                                    
\     \____/ __ \\   /\  ___/                                    
 \______  (____  /\_/  \___  >                                   
        \/     \/          \/                                    
   _____       .___                    __                        
  /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____  
 /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \ 
/    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/ 
\____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >
        \/      \/           \/     \/                        \/
        """)

def intro():
    print("Welcome to Raspi's cave adventure")
    print("""
    It is the Dark Ages, the time of stone castles, knights with swords,
    and some say mythical beasts that breathe fire.  Our main character is
    a young boy named, Raspi .  One day Raspi is off gathering firewood when
    he finds himself lost in the woods.  He stumbles upon the entrance to a
    cave.  He peers in the entrance and finds that the cave splits into a
    left tunnel and a right tunnel.  He remembers a folk tale his grandmother
    used to tell of a mysterious cave in this very forest that holds enormous
    treasures.  It is said the treasure is guarded by a ferocious
    fire-breathing dragon.  Raspi can't resist the temptation to explore the
    cave and although he wants to turn back, he walks slowly into the dark
    cave.
    """)

def left_or_right():
    print("You see the cave split into a left and right tunnel")
    time.sleep(2)
    print("Do you choose to go left or right?")
    time.sleep(2)
    choice = input("Enter L for left or R for right: ").upper()
    time.sleep(2)
    return choice

# Displays text describing the player's demise and a game over message			
def wrong_answer():										
    print("You seem to have trouble making good decisions!")
    time.sleep(2)
    print("Suddenly a stalactite falls from the ceiling and bonks you on the head.")
    time.sleep(2)
    print("Game Over!!!")

def left_cave():
    print("You walk into the left cave.  It is cold and dark.")
    time.sleep(2)
    print("The cave opens up to a large room with an underground river.")		
    time.sleep(2)
    print("You notice a small boat on the edge of the river.")
    print("Do you use the boat, swim, or walk along the side of the river?")
    time.sleep(2)
    river_choice =  input("Enter B for boat, S for swim, or W for walk: ").upper()
    time.sleep(2)
    return river_choice

def boat():
    # You hop in the boat
    print("You step in the boat and start drifting down the river.")
    time.sleep(2)
    print("It's too late when you realize that your boat has a hole in it.")
    time.sleep(2)
    print("The boat sinks and you sink with it!")
    time.sleep(2)
    print("Game Over!!!")

def swim():
    print("You dive into the water and start swimming down the river.")
    time.sleep(2)
    print("You swim along the river for many minutes before climbing onto a bank.")
    time.sleep(2)
    print("Just then, you spot a cave with a twinkling light")
    time.sleep(2)
    print("Wait... that isn't a torch!")
    time.sleep(2)
    print("You've found the hidden treasure cave!  It is filled with gold and gems.")
    time.sleep(2)
    print("You live happily ever after...")

def walk():
    print("You walk along the narrow edge of the river.")
    time.sleep(2)
    print("You start walking along the edge, but it is very dark.")
    time.sleep(2)
    print("You suddenly trip on a rock.")
    time.sleep(2)
    print("The last thing you remember is hitting your head on a rock.")
    time.sleep(2)
    print("Game Over!!!")

def right_cave():
    print("You walk into the right cave.  The cave starts sloping downward.")
    time.sleep(2)
    print("You come to a room with a large hole in the floor.")
    time.sleep(2)
    print("To your right, you notice a rope leading down the hole.")
    time.sleep(2)
    print("To your left, you see a long hallway with a torch at the end.")
    time.sleep(2)
    print("Do you climb down the rope or go towards the torch light?")
    time.sleep(2)
    hole_choice = input("Enter R for rope or T for torch: ").upper()
    return hole_choice

def hole():
    print("You slowly climb down the rope, eventually reaching the bottom.")
    time.sleep(2)
    print("You look around and see that you are in a dragon's lair.")
    time.sleep(2)
    print("To your left, you see a small dark room.")
    time.sleep(2)
    print("To your right, you see the dragon sleeping.")
    time.sleep(2)
    print("Do you try to slay the dragon or go into the dark room?")
    time.sleep(2)
    dragon_choice = input("Enter S for slay the dragon or R for room: ").upper()
    time.sleep(2)
    return dragon_choice

def room():
    print("You walk enter the dark room.")
    time.sleep(2)
    print("You raise your torch to look around...")
    time.sleep(2)
    print("and find that you are in a treasure room!")
    time.sleep(2)
    print("You've found the hidden treasure cave!  It is filled with gold and gems.")
    time.sleep(2)
    print("You live happily ever after.")

def slay():
    print("You draw your sword and raise it high above your head.")
    time.sleep(2)
    print("Just then the dragon opens one eye.")
    time.sleep(2)
    print("Before you can even react, it opens its mouth and eats you whole.")
    time.sleep(2)
    print("Game Over!!!")

def torch():
    print("You pass around the outside edge of the hole and head towards the torch light.")
    time.sleep(2)
    print("You come closer to the light and see you're in a cave full of crystals.")
    time.sleep(2)
    print("Suddenly a large crystal falls from the ceiling, crushing you.")
    time.sleep(2)
    print("Game Over!!!")

play_again = "Y"

# Main Program
while play_again.upper() == "Y":
    title()
    time.sleep(2)
    intro()
    time.sleep(2)

        
    # 1st Choice: Left or Right Cave?
    choice = left_or_right()
    if choice == "L" or choice == "LEFT":
        # You walk into the Left cave
        choice = left_cave()
        if choice == "W" or choice == "WALK":					
            # You walk along the edge of the river
            walk()
        elif choice == "B" or choice == "BOAT":
            # You get in the boat
            boat()          
        elif choice == "S" or choice == "SWIM":					
            # You jump in the water and start swimming
            swim()
        else:
            # Wrong answer
            wrong_answer()
    elif choice ==  "R" or choice == "RIGHT":
        # You walk in the right cave
        choice = right_cave()
        if choice == "T" or choice == "TORCH":
            # You walk towards the torch light
            torch()
        elif choice == "R" or choice == "ROPE":
            # You climb down the rope
            choice = hole()
            if choice == "S" or choice == "SLAY":
                # You try to slay the dragon
                slay()
            elif choice == "R" or choice == "ROOM":
                # You enter the dark room
                room()
            else:
                # Wrong answer
                wrong_answer()
        else:
            # Wrong answer
            wrong_answer()
    else:
        # Wrong answer
        wrong_answer()
        
    # Check if user wants to play again
    print("Do you want to play again?")
    play_again = input("Enter Y for yes or N for no: ")
    
