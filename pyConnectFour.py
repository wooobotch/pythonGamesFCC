import numpy as np

#We'll start from the board design
def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
print(board)


#main game loop
game_over = False
turn = 0

while not game_over:
    #Ask for players input
    if turn == 0:
        selection = int(input("Player 1 - Your turn - Select (0-6):"))
        #We need to cast it to int because the input is a string
    else:
        selection = int(input("Player 2 - Your turn - Select (0-6):"))
    turn += 1
    turn = turn % 2

# 01:43:10
