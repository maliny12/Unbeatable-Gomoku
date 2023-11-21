board = [[ "unoccupied" for i in range(9)] for j in range(9)]

"""
board[1][6] = "⚫"
board[2][6] = "⚫"
board[3][6] = "⚫"
board[4][6] = "⚫"
board[5][6] = "⚫"

board[0][0] = "⚫"
board[0][1] = "⚫"
board[0][2] = "⚫"
board[0][3] = "⚫"
board[0][4] = "⚫"
board[0][8] = "⚫"

board[1][6] = "⚫"
board[2][6] = "⚫"
board[3][6] = "⚫"
board[4][6] = "⚫"
board[5][6] = "⚫"

"""
board[0][8] = "⚫"
board[1][7] = "⚫"
board[2][6] = "⚫"
board[3][5] = "⚫"
#board[4][4] = "⚫"

board_size = 9

def check_available_move(board):
        available = []
        for i in range(board_size):
                for j in range(board_size):
                        if not is_occupied(board,i,j):
                                available.extend([(str(i),chr(j + 65))])
        return(available)

def is_occupied(board, x,y):
        if board[x][y] != "unoccupied":
                return True
        else:
                return False

# Transposed board 
transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
#print(transposed_board)

# Mirror board (vertically)
mirror_board = [list(reversed(row)) for row in board]
#print(mirror_board)

def check_winner(board, stone) :

    winner = None

     # Check rows
    for row in board:
        for elem in range(len(row) - 4):
            if all([s == stone for s in row[elem:(elem + 5)]]):
                winner = True
                break  # Stop checking when the winner is found
        #print(row)


    # for column check
    for col in transposed_board:
        for elem in range(len(transposed_board) - 4):
            if all([s == stone for s in col[elem: (elem + 5)]]):
                winner = True
                break # Stop checking when the winner is found
        #print(col)
    

    # For diagnoal check (one direction)
    for row in range(len(board) - 4):
        for col in range(len(board) - 4):
            dia_list = [board[row + offset][col + offset] for offset in range(5)]
            if all([s == stone for s in dia_list]):
                winner = True
                break # Stop checking when the winner is found
    
    # For diagnoal check (the other direction)
    for row in range(len(mirror_board) - 4):
        for col in range(len(mirror_board) - 4):
            dia_list = [mirror_board[row + offset][col + offset] for offset in range(5)]
            if all([s == stone for s in dia_list]):
                winner = True
                break # Stop checking when the winner is found

    if winner:
         return stone
    elif check_available_move(board) == [] :
         return "Draw"
    else:
         return "None"

        
#print(check_available_move(board))

print(check_winner(board, '⚫'))





     

