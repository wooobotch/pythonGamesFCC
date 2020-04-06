import numpy as np
FILAS = 6
COLUMNAS = 7

#We'll start from the board design
def create_board():
    board = np.zeros((FILAS,COLUMNAS))
    return board

def drop_piece(board, fila, columna, pieza):
    board[fila][columna] = pieza

def is_valid_location(board, columna):
    return board[FILAS - 1][columna] == 0

def get_next_open_row(board, columna):
    for f in range(FILAS):
        if board[f][columna]:
            return f

def print_board(board):
    print (np.flip(board, 0))

def winning_move(board, pieza):
    #We look for horizontal locations for a winning combo
    #The limits are set to COLUMNAS-3 because otherwise there
    #wouldn't be room for enought pieces (4) to make a winning connection
    for c in range(COLUMNAS -3):
        for f inrange(FILAS):
            if board[f][c] == piece and board[f][c+1] == piece and board[f][c+2] == piece and board[f][c+3] == piece
                return True

    #The same we did before, this time the limit is set for the rows
    for c in range(COLUMNAS):
        for f inrange(FILAS-3):
            if board[f][c] == piece and board[f+1][c] == piece and board[f+2][c] == piece and board[f+3][c] == piece
                return True

    #We'll analize diagonal connections according to it's slope
    #The same criteria for a reduced range is applied
    #Positively sloped diagonal
    for c in range(COLUMNAS-3):
        for f inrange(FILAS-3):
            if board[f][c] == piece and board[f+1][c+1] == piece and board[f+2][c+2] == piece and board[f+3][c+3] == piece
                return True

    #Positively sloped diagonal
    for c in range(COLUMNAS-3):
        for f inrange(3, FILAS):
            if board[f][c] == piece and board[f-1][c+1] == piece and board[f-2][c+2] == piece and board[f-3][c+3] == piece
                return True

board = create_board()
print(board)


#main game loop
game_over = False
turn = 0

while not game_over:
    #Ask for players input
    if turn == 0:
        columna = int(input("Player 1 - Your turn - Select (0-6):"))
        #We need to cast it to int because the input is a string

        if is_valid_location(board, columna):
            fila = get_next_open_row(board, columna)
            drop_piece(board, columna, fila, 1)
        if winning_move(board, 1):
            print("All your base are belong to player One!!!1")
            game_over = True
            break

    else:
        columna = int(input("Player 2 - Your turn - Select (0-6):"))


        if is_valid_location(board, columna):
            fila = get_next_open_row(board, columna)
            drop_piece(board, columna, fila, 2)
        if winning_move(board, 2):
            print("All your base are belong to player Two!!!1")
            game_over = True
            break

    #The break statement in the end of the "if winning move" call exits the current interation
    #preventing from printing another board after a player wins
    print_board(board)

    turn += 1
    turn = turn % 2

# 02:07:24
