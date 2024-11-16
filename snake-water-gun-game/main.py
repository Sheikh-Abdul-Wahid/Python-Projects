# Lets consider -1 = water, 0 = gun & 1 = snake 

import random                            # Import random module to make computer's choice random
you_dict = {"s": 1, "w": -1, "g": 0}     # Dictionary to map the characters to values
computer = random.choice([-1, 0, 1])     # Computer randomly chooses between snake, water, or gun
you_string = input("Enter the char(s for Snake, w for Water, g for Gun): ")   # User input

if you_string.lower() not in you_dict:   # Validate the user input: check if it's 's', 'w', or 'g'
    print("Invalid input. Please enter 's', 'w', or 'g'.")
    exit()  # Exit the program if input is invalid

you = you_dict[you_string.lower()]       # Map the valid input to its numerical equivalent
reverse_dict = {1: "s", -1: "w", 0: "g"} # Reverse map to show user-friendly output

# Print choices of both computer and user
print(f"Computer Chose: {reverse_dict[computer]} \nYou Chose: {reverse_dict[you]}")

if computer == you:
    print("It's a Draw!")
else:
    if (computer == -1 and you == 1):    # Snake drinks Water
        print("You Win!")
    elif (computer == -1 and you == 0):  # Water spoils Gun
        print("You Lose")
    elif (computer == 1 and you == 0):   # Gun shoots Snake
        print("You Win!")
    elif (computer == 1 and you == -1):  # Snake drinks Water
        print("You Lose")
    elif (computer == 0 and you == 1):   # Gun shoots Snake
        print("You Lose")
    elif (computer == 0 and you == -1):  # Water spoils Gun
        print("You Win!")
    else:
        pass





















