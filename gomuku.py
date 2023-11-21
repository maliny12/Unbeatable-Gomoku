# Import library
import random

####
# game menu

def game_menu(first_run):
       
       print("\n\n Welcome to Gomoku !!!\n")

       if first_run:
                print("Gomoku is a two-player board game aiming to connect five stones in a row either vertically, horizontally, or diagonally on a grid.")
                enter = input("Press any key start game.")

                return '1'
       else:
                print("1. Start game.")
                print("2. Print the board.")
                print("3. Place a stone.")
                print("4. Reset the game.")
                print("5. Exit.\n")

       while True:
                choice = input("Enter a choice (1/2/3/4/5) : ")
                
                if choice not in ['1', '2','3','4','5']:
                        print("\nPlease enter a valid entry.\n")
                        continue # continue the loop until valid entry is entered

                return choice # returns the user choice 
       

#####
# Create a board
board = [] # Board is an array of "unoccupied", "⚫" and "⚪️" 

def create_board() : 
        board.clear()

        wrong_input = True 
        # Create a board

        while wrong_input :
                print("\nPlease choose the dimension of the board. ")
                print("Enter 9 for 9x9 board.")
                print("Enter 13 for 13x13 board.")
                print("Enter 15 for 15x15 board.\n")

                global board_size # declare board_size as a global variable
                

                try :
                       board_size = int(float(input("Enter the size of the board: ")))
                except:
                        board_size = -1
                

                if board_size not in [9,13,15]:
                        print("\nPlease choose a valid dimension")
                        continue 
                else:
                        print("\nYour board is being created.")
                        board.extend([[ "unoccupied" for i in range(board_size)] for j in range(board_size)]) 
                        wrong_input = False # Change wrong_input to false and stop the loop.

# Board for asethic purposes
# Row Label
col_label = {
  9 : "A   B   C   D   E   F   G   H   I",
  13: "A   B   C   D   E   F   G   H   I   J   K   L   M",
  15: "A   B   C   D   E   F   G   H   I   J   K   L   M   N   O"
}

# Create a dynamic board
def print_board() :
        
        print(col_label[board_size])
        board_string = ""
        i = 0
        for x in range(board_size):
                for y in range(board_size):

                        # Add row elements
                       
                        if board[x][y] != 'unoccupied':
                            board_string += board[x][y]
                        else:
                            board_string += "  "

                        if y != board_size - 1:
                               board_string += "--"
                
                board_string += "   " + str(x) + "\n" 
                

                if x < board_size - 1:
                        board_string += "|   " * board_size + "\n"
                
        #board_string += "  --"*(board_size-1) + "     " + str(i)
        

        print( board_string)



#####
# Function to check if the position is occupied
def is_occupied(board, x,y):
        if board[x][y] != "unoccupied":
                return True # The position is available
        else:
                return False # The position is occupied
        


# Funtion for player and bot placement
def place_on_board(board, stone, position):

        try: 
                #convert position to x, y
                position_list = position.split()
                x = int(position_list[0]) 
                y = ord(position_list[1]) - 65 # To make it starts from 0 

                # Check if position on board is occupied
                if is_occupied(board, x, y): 
                        return False
                else:
                        board[x][y] = stone
                        return True

        except (IndexError, ValueError):
               return False
        

        


# Funtion to check available postion       
def check_available_move(board):
        available = []
        for i in range(board_size):
                for j in range(board_size):
                        if not is_occupied(board,i,j):
                                available.extend([(str(i),chr(j + 65))])
        return(available)



# Function to check for winner

def check_winner(board, stone) :
    
    #Set winner to none
    winner = None

    #Transposed board
    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]

    # Mirror board (vertically)
    mirror_board = [list(reversed(row)) for row in board]

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
         return stone # If there is a winner, return the winning stone
    elif check_available_move(board) == [] :
         return "Draw" # return "Draw" if there are no space left on the board
    else:
         return "None" # return "None" if there are no winner, yet
    
######
# Random computer player
 
# Bot positon based on the last player's move   

def random_computer_player(board, player_move):

        position = player_move.split(" ")

        # Get the coordinate of the latest player move
        player_x = int(position[0])
        player_y = ord(position[1]) - 65


        # Find neighboring positon based on player's move
        neighbour = []
        for i in range(board_size):
                for j in range(board_size):
                        if (abs(i - player_x ) <= 1) and (abs(j - player_y ) <= 1):
                                if not (i == player_x and j == player_y):
                                        if not is_occupied(board, i, j):
                                                neighbour.append([i,j])
        

        if len(neighbour) == 0:
                bot_position = random.choice(check_available_move(board)) # 3 A
        else:
                bot_position = random.choice(neighbour)  # 3 3
                bot_position[1] = chr(bot_position[1] + 65)
                
        
        #Update Board with bot position
        board[int(bot_position[0])][ord(bot_position[1]) - 65] = "⚪️"
      
        return (bot_position[0],bot_position[1])





def game_play():
       
       first_run = True 
       game_op  = True # Game Operating
       winner_or_draw = False


       while game_op and not winner_or_draw:
                
                game_menu_choice = game_menu(first_run)

                if game_menu_choice == '1':
                        if first_run:
                               
                               first_run = False

                               create_board()

                               print("\nChoose your mode!!!")
                               print("Option 1: Multi-player")
                               print("Option 2: Player vs. Robot")
                               while True:
                                        mode = input("\nEnter your game mode (1 or 2): ")
                                        if mode not in ['1', '2']:
                                                print("\nPlease enter a valid entry.")
                                                continue
                                        else: 
                                               print("Mode", mode, "chosen.","\n")
                                               print("\nNow you are ready to play the game.")
                                               print("\nTo start the game, enter 3 to place the stone.\nAlternatively, you can enter 2 to visualise the board.\n")
                                               enter = input("Press any key to continue.")
                                               break
                                               
                        else:
                               print("\nDo you wish to restart or exit the game?")
                               print("Enter 1 to restart the game.")
                               print("Enter 2 to exit the game\n")
                               while True:
                                        entry = input("Select an option (1 or 2): ")
                                        if mode not in ['1', '2']:
                                                print("\nPlease enter a valid entry.")
                                                continue
                                        
                                        
                                        if entry == "1":
                                               first_run = True
                                               break


                                        else:
                                               game_op = False
                                               break
                elif game_menu_choice == "2":
                       print("\nGomoku board\n ")
                       print_board()

                elif game_menu_choice == "3":
                        if mode == "1":
                              if multi_player_mode() != 'No Winner':
                                     winner_or_draw = False
                                     break
                        else:
                               if player_vs_robot_mode() != 'No Winner':
                                     winner_or_draw = False
                                     break
                
                elif game_menu_choice == "4":
                       first_run = True

                
                else:
                       game_op = False


       print("\nWe are sad to see you go :(")
       print("Thank you for playing Gomoku !!! ")


def multi_player_mode():

        round_over = False
        winner= False
        draw = False

        print("\nWelcome to muli-player mode.")
        print("Player with ⚫ stone will open first.")
        print("To enter your position enter your selected row number and column name seperated by ' '. ")
        print("(For example: '3 A' to place a stone at row 3 and column A. \n")

        #player 1
        while not round_over or winner or draw:
                print("⚫ turn.\n")
                p1_position = input("Please enter your positon: ")
        
                if not place_on_board(board,"⚫", p1_position) :
                        print("\nUnable to place a stone at this position. Please try again.")
                        print("Here are all the available positions:")
                        print(check_available_move(board))
                        continue

                if check_winner(board,"⚫") == "⚫" :
                       print("⚫ is the winner.")
                       winner = True
                       break
                elif check_winner(board,"⚫") == "Draw":
                       print("Draw. There is no winner.")
                       draw = True
                else:
                       pass

                print_board()
                        
                       

                #player 2
                while not round_over or winner or draw:
                        print("\n⚪️ turn.\n")
                        p2_position = input("Please enter your positon: ")
                
                        if not place_on_board(board,"⚪️", p2_position) :
                                print("\nUnable to place a stone at this position. Please try again.")
                                print("Here are all the available positions:")
                                print(check_available_move(board))
                                continue

                        if check_winner(board,"⚪️") == "⚪️" :
                                print("⚪️ is the winner.")
                                winner = True
                                break
                        elif check_winner(board,"⚪️") == "Draw":
                                print("Draw. There is no winner.")
                                draw = True
                        else:
                                pass
                        
                        print("\n⚫ last move is", p1_position)
                        print("⚪️ last move is", p2_position, '\n')
                        print_board()
                        enter = input("\nPress any key to return to the game menu.")
                        round_over = True

        if winner or draw:
               return 'Stop the game.'
        else:
               return 'No Winner'


def player_vs_robot_mode():

        round_over = False
        winner= False
        draw = False

        print("\nWelcome to Player vs. Bot mode.")
        print("You will open first with a ⚫ stone.")
        print("To enter your position enter your selected row number and column name seperated by ' '. ")
        print("(For example: '3 A' to place a stone at row 3 and column A. \n")

        #player 1
        while not round_over or winner or draw:

                print("⚫ turn.\n")
                position = input("Please enter your positon: ")
        
                if not place_on_board(board,"⚫", position) :
                        print("\nUnable to place a stone at this position. Please try again.")
                        print("Here are all the available position:")
                        print(check_available_move(board))
                        continue

                if check_winner(board,"⚫") == "⚫" :
                       print("⚫ is the winner.")
                       winner = True
                       break
                elif check_winner(board,"⚫") == "Draw":
                       print("Draw. There is no winner.")
                       draw = True
                else:
                       pass

                print_board()
        

                #Robot
                print("\n🤖 turn.\n")
                player_move = position
                print("⚫ last move is", position)
                print("The bot 🤖 has placed a ⚪️ stone at ", random_computer_player(board, player_move))

                if check_winner(board,"⚪️") == "⚪️" :
                        print("⚪️ is the winner.")
                        winner = True
                        break
                elif check_winner(board,"⚪️") == "Draw":
                        print("Draw. There is no winner.")
                        draw = True
                else:
                        pass

                print_board()
                enter = input("\nPress any key to return to the game menu.")
                round_over = True

        if winner or draw:
               return 'Stop the game.'
        else:
               return 'No Winner'

game_play()
                                                
