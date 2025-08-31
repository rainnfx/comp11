import random

# 1 rock 2 paper 3 scissors
robotChoice = random.randrange(1, 4)

print("Make your choice player!")
print("[a] Rock\n[b] Paper\n[c] Scissors")
choice = input("Choice: ")

# map player choice to a number
if choice == "a":
    playerChoice = 1
elif choice == "b":
    playerChoice = 2
elif choice == "c":
    playerChoice = 3
else:
    print("Invalid choice!")
    exit()

# show robots choice
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
print("Robot chose:", choices[robotChoice])
print("You chose:", choices[playerChoice])

# decide the winneer
if playerChoice == robotChoice:
    print("It's a tie!")
elif (playerChoice == 1 and robotChoice == 3) or \
     (playerChoice == 2 and robotChoice == 1) or \
     (playerChoice == 3 and robotChoice == 2):
    print("You win!")
else:
    print("Robot wins!")

