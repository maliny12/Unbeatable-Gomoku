

import random
# Create Board 
# Board is an array of "unoccupied", "⚫" and "⚪️" 
board = []

"""
def create_board() :

        wrong_input = True

        while wrong_input :
                print("Please choose the dimension of the board. ")
                print("Enter 9 for 9x9 board.")
                print("Enter 13 for 13x13 board.")
                print("Enter 15 for 15x15 board.")

                global board_size # declare board_size as a global variable
                board_size = int(float(input("Enter the size of the board: ")))

                if board_size not in [9,13,15]:
                        print("Please choose a valid dimension")
                        continue
                else:
                        print("Your board is being created.")
                        board.extend([[ "unoccupied" for i in range(board_size)] for j in range(board_size)])
                        wrong_input = False
                        
create_board()

#print(board)
#print(board_size)


#board[0][1] = "B"
#print(board)
# Function to check if the position is occupied
def is_occupied(board, x,y):
        if board[x][y] != "unoccupied":
                return True
        else:
                return False
        
#print(is_occupied(board, 0, 1))


# Funtion to check available postion       
def check_available_move(board):
        available = []
        for i in range(board_size):
                for j in range(board_size):
                        if not is_occupied(board,i,j):
                                available.extend([(str(i),chr(j + 65))])
        return(available)


        

def player_moves() :
        
        invalid_input = True

        while True:
                # Player Input
                print("Input to select location.")
                print("Make select a row number between 0 to 8.")
                row_value = int(input(" Enter row: "))
                if not row_value in range(8):
                        print("Invalid input. Please select a row number between 0 to 8.")
                        continue
        
                print("Make a selection (A to H) for column.")
                col_value = ord(input("Enter column: ")) - 65



# Funtion for player and bot placement
def place_on_board(board, stone, position):

        #convert position to x, y
        list = position.split()
        x = int(list[0])
        y = ord(list[1]) - 65

         # Check if position on board is occupied
        if is_occupied(board, x, y): 
                return False
        else:
                board[x][y] = stone
                return True
                

# Create a dynamic board
def format_row(board_row) :
        row = " " # empty space on the board
        for elem in board_row:
                if elem != "unoccupied":
                        row += str(elem)
                else:
                        row += " "
        return " " + ("--" + " ")*(len(board_row) - 1)


def format_col():
        return ("|" + "  ")*(board_size - 1) + "|"

def print_board(board):
        for i in range(board_size):
                print(format_row(board[i]))
                print(format_col())
        print(format_row(board[board_size - 1]))

place_on_board(board, "⚫", ("1 D"))


col_label = {
  9 : "A   B   C   D   E   F   G   H   I",
  13: "A   B   C   D   E   F   G   H   I   J   K   L   M",
  15: "A   B   C   D   E   F   G   H   I   J   K   L   M   N   O"
}

# Create a dynamic board
def format_board() :
        
        print(col_label[board_size])
        board_string = ""
        i = 0
        for x in range(board_size):
                for y in range(board_size -1 ):

                        # Add row elements
                       
                        if board[x][y] != 'unoccupied':
                            board_string += board[x][y] + "--"
                        else:
                            board_string += "  --"
                
                board_string += "   " + str(i) + "\n" 
                


                if y < len(board):
                        board_string += "|   " * board_size + "\n"
                
                i += 1
                
        board_string += "  --"*(board_size-1) + "   " + str(i)
        

        return board_string



'''
def format_row(board_row) :
    row = " "  # empty space on the board
    for elem in board_row:
        if elem != 'unoccupied':
            row += str(elem)
        else:
            row += " "
    return " " + ("--" + "X")*(len(board_row) - 1)
'''
def format_col():
    return ("|" + "  ")*(board_size - 1) + "|"

def print_board(board):
    for i in range(board_size):
        print(format_board())
        print(format_col())
    print(format_board())

place_on_board(board, "⚫", ("1 G"))
place_on_board(board, "⚪️", ("2 D"))

#print(format_board())

#print(check_available_move(board))

def bot_placement(board, player_move):

        # Get the coordinate of the latest player move
        player_x = int(player_move[0])
        player_y = ord(player_move[1]) - 65


        # Find neighboring positon based on player's move
        neighbour = []
        for i in range(9):
                for j in range(9):
                        if (abs(i - player_x ) <= 1) and (abs(j - player_y ) <= 1):
                                if not (i == player_x and j == player_y):
                                        if not is_occupied(i, j):
                                                neighbour.append([i,j])
        if len(neighbour) == 0:
                bot_position = random.choice(check_available_move(board))
        else:
                bot_position = random.choice(neighbour)
                
        #Update Board with bot position
        board[int(bot_position[0])][ord(bot_position[1])-65] = "⚪️"
      
        return (bot_position[0],bot_position[1])

#print(bot_placement(board,("5 A")))
#print(format_board())
"""

def game_menu():
       print(" Welcome to Gomoku !!!")
       print("Please choose an option.")
       print("1. Start game.")
       print("2. Print the board.")
       print("3. Place a stone.")
       print("4. Reset the game.")
       print("5. Exit.")

       while True:
                choice = input("Enter a choice (1/2/3/4/5) : ")
                
                if choice not in ['1', '2','3','4','5']:
                        print("Please enter a valid entry.")
                        continue

                return choice














                        




                        


                

        
                      
        
               

        


       
       

