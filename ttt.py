import random
import numpy as np

#^ --------- Global Variables -----------#
game_start = ""
user_marker, computer_marker = "", ""
player1, player2 = "", ""
player_vs_com = ""

#^ Player user input
def TicTacToe_game():
    global game_start, user_marker, computer_marker, player1, player2, player_vs_com
    while game_start.upper() not in ["Y","N"]:   
        game_start = input("Welcome to Tic-Tac-Toe, wanna play? (Y or N)")
        
        #! Ask's user if they want to play or not
        if game_start.upper() not in ["Y","N"]:
            print("Sorry, I dont understand, please choose Y or N")
        elif game_start.upper() == "N":
            print("Ok Then Have A Nice Day!")
        elif game_start.upper() == "Y":
            game_start = "Y"
            print("Great now for 3 more questions")
            
            #! asking for player symbol and if they want to go first(transition)
            while user_marker not in ["X","O"]: 
                user_marker = input("Do you wanna be X or O?").upper()
                if user_marker not in ["X","O"]:
                    print("Sorry, Thats not a valid marker. Please try again")
                else:
                    if user_marker == "X": computer_marker = "O"
                    else: computer_marker = "X"
                    
                    #! Asking if user wants to go first or second(transition)
                    while player1 not in ["1","2"]:
                        player1 = input("Do you wanna go 1st or 2nd? (1 or 2)")
                        if player1 not in ["1","2"]:
                            print("Please Try Again")
                        else:
                            if player1 == "1": player1, player2 = "1","2"
                            else: player1, player2 = "2","1" 
                            
                            #! Asking if user wants to go against computer or player
                            while player_vs_com.upper() not in ["P","C"]:  
                                player_vs_com = input("Player vs. Player(P) or Player vs. Computer(C)")
                                if player_vs_com.upper() not in ["P","C"]:
                                    print("Sorry, I dont understand, please choose P or C")
                                elif player_vs_com.upper() == "P": player_vs_com = "P"
                                else: player_vs_com = "C"
                                print("Ok Let the game begin!")
                                               
#^ Board function
TicTacToe = ['f', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def ttt_board():
    print(f"Player 1: {user_marker} \tvs\tPlayer 2: {computer_marker}");
    print("     |     |     ");
    print("  " + TicTacToe[1] + "  |  " + TicTacToe[2] + "  |  " + TicTacToe[3] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TicTacToe[4] + "  |  " + TicTacToe[5]+"  |  " + TicTacToe[6] + "  ")
    print("_____|_____|_____");
    print("     |     |     ");
    print("  " + TicTacToe[7] + "  |  " + TicTacToe[8]+"  |  " + TicTacToe[9] + "  ")
    print("     |     |     ");

#^ Player input functions
def player1_input():
    ttt_board()
    p1_positon = ""
    while TicTacToe:
        p1_positon = input("Ok Player 1, Input a available positon (1-9):")
        if p1_positon.isnumeric() == False: 
            print("Sorry, that is not a number. Please Try Again")
        elif p1_positon not in TicTacToe:
            print("Sorry that position isn't available. Please Try Another one")
        else:
            TicTacToe[int(p1_positon)] = user_marker
            break
    return ttt_board()

def player2_input():
    ttt_board()
    p2_positon = ""
    while TicTacToe:
        p2_positon = input("Ok Player 2, Input a available positon (1-9):")
        if p2_positon.isnumeric() == False: 
            print("Sorry, that is not a number. Please Try Again")
        elif p2_positon not in TicTacToe:
            print("Sorry that position isn't available. Please Try Another one")
        else:
            TicTacToe[int(p2_positon)] = computer_marker
            break
    return ttt_board()

#^ Check board to see if there's tie, Continue or winner
def table_check(table):
    board = [table[1::][i:i+3] for i in range(0, len(table[1::]), 3)]
    hori = "".join(["".join(set(i)) for i in board if len(set(i)) == 1])

    #* Check's list for vertical rows
    vert = [[lst[i] for lst in board] for i in range(len(board))]
    vert = "".join(["".join(set(l)) for l in vert if len(set(l)) == 1])

    #* Check's list for diagonal rows
    diag = [set(np.diagonal(board)), set(np.diagonal(np.fliplr(board)))]
    diag = "".join(["".join(d) for d in diag if len(d) == 1])
    final_check = [ans for ans in [hori,vert,diag] if len(ans) == 1]
    
    #*Check's for Tie, None(No current winner continue), and X or Y
    digit_check = any(t.isdigit() for t in "".join(table[1::]))
    if digit_check == False and len(final_check) == 0: return "Tie"
    elif digit_check == True and len(final_check) == 0: return None
    else: return final_check[0]

#^ For Player Vs. Computer (Computer moves)
def computer_input(table):
    board = table[1::]
    winning_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], 
                         [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    p1_positions = [i+1 for i in range(len(board)) if board[i] == user_marker]
    
    #* If Computer starts second
    if len(p1_positions) == 1:
        p1_positions = p1_positions[0]
        possible_wins = [wp for wp in winning_positions if p1_positions in wp]

        possible_wins = [pw2 for pw1 in possible_wins for pw2 in pw1 if pw2 != p1_positions]
        
        com_position = random.choice(possible_wins)
        TicTacToe[com_position] = computer_marker
        return ttt_board()
    
    #* Checks to see if two in a row but also
    #* makes sure theres one available position 

    def check_two():
        if len(p1_positions) != 2: return 0
        else:
            row = [wp for wp in winning_positions if wp.count(p1_positions[0]) and wp.count(p1_positions[1])][0]    
            if any(row): return any([table[r].isnumeric() for r in row])
            else: return 0 

    #* Blocks player if they gets 2 in a row
    if len(p1_positions) == 2 and check_two():
        current_strategy = [wp for wp in winning_positions if wp.count(p1_positions[0]) and wp.count(p1_positions[1])]
        com_position = [i for i in sum(current_strategy, []) if i not in p1_positions][0]
        TicTacToe[com_position] = computer_marker
        return ttt_board()
    
    #* if computer starts first
    elif int(player1) == 2 or len(p1_positions) > 2:
        available_positions = [i for i in table if i.isnumeric()]
        com_position = int(random.choice(available_positions))
        TicTacToe[com_position] = computer_marker
        return ttt_board()

#^ interpets the result of table_check and ends the 
#^ game doing on of these commands

def table_result():
    if table_check(TicTacToe) == user_marker:
        print("Hip Hip Hooray, Player 1 You have won!!!")
    elif table_check(TicTacToe) == computer_marker:
        print("Hip Hip Hooray, Player 2 You have won!!!")
    elif table_check(TicTacToe) == "Tie":
        print("Tie Game, nobody wins") 

#^ --------- Finished Product(game) -----------#

while True:
    TicTacToe_game()
    if game_start.upper() == "N": break
    
    #* Player1 vs Player 2
    if player_vs_com == "P":
        player1_input()
        if table_check(TicTacToe): break
        player2_input()
        if table_check(TicTacToe): break
    
    elif player_vs_com == "C":
        if int(player1) == 1:
            player1_input()
            if table_check(TicTacToe): break
            computer_input(TicTacToe)
            if table_check(TicTacToe): break
        
        elif int(player1) == 2:
            computer_input(TicTacToe)
            if table_check(TicTacToe): break
            player1_input()
            if table_check(TicTacToe): break
table_result()     