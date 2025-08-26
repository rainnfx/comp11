# 5x5 grid 2 player battle ship

# create empty 5x5 grids for both players
playerOneGrid = [[0 for _ in range(5)] for _ in range(5)]
playerTwoGrid = [[0 for _ in range(5)] for _ in range(5)]

# function to get valid coords from players
def get_coordinate(player, axis):
    while True:
        try:
            coord = int(input(f"{player}, enter {axis} coordinate (1-5): "))
            if 1 <= coord <= 5:
                return coord - 1  # convert to 0-indexed
            else:
                print("Invalid coordinate! Must be between 1 and 5.")
        except ValueError:
            print("Please enter a number!")

# players place their ships
print("Player 1, place your ship:")
playerOneShipX = get_coordinate("Player 1", "X")
playerOneShipY = get_coordinate("Player 1", "Y")
playerOneGrid[playerOneShipY][playerOneShipX] = 1

print("Player 2, place your ship:")
playerTwoShipX = get_coordinate("Player 2", "X")
playerTwoShipY = get_coordinate("Player 2", "Y")
playerTwoGrid[playerTwoShipY][playerTwoShipX] = 1

# init game state
playerOneSunk = False
playerTwoSunk = False
shotsFired = 0

print("\nGame Start!\n")

# main game loop
while not (playerOneSunk or playerTwoSunk):
    # player 1s turn
    print("Player 1's turn:")
    x = get_coordinate("Player 1", "X")
    y = get_coordinate("Player 1", "Y")
    shotsFired += 1
    if playerTwoGrid[y][x] == 1:
        print("Hit! Player 1 sunk Player 2's battleship!")
        playerTwoSunk = True
        break
    else:
        print("Miss!\n")

    # player 2s turn
    print("Player 2's turn:")
    x = get_coordinate("Player 2", "X")
    y = get_coordinate("Player 2", "Y")
    shotsFired += 1
    if playerOneGrid[y][x] == 1:
        print("Hit! Player 2 sunk Player 1's battleship!")
        playerOneSunk = True
        break
    else:
        print("Miss!\n")

print(f"Game Over! Total shots fired: {shotsFired}")
