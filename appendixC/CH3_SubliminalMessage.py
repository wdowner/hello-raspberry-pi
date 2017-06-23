# Subliminal Messages
# Ryan Heitz
# Puts a hidden message in a set of characters

title = "Subliminal Messages"
print("*" * 80)
print(title)
print("*" * 80)

# Gather input from the player
player_name = input("Enter your name: ")
thing = input("Enter the name of something you want: ")
weird_characters = "*#ad@32*)23 )@*sad# 2&^ 32^423!"

# Create the message
message = "You really want to buy " + player_name + " a " + thing + "."

# Hide it between the weird characters
print(weird_characters * 10 + message + weird_characters * 10)

