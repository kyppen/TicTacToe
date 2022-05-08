#Tic Tac Toe game assigment from udemy course:
#By Sondre Fagerhus
#Date 7/5/2022


#Creating the board

row1 = ["E","E","E"]
row2 = ["E","E","E"]
row3 = ["E","E","E"]

winner = ""

players_turn = []

player1 = "X"
player2 = "O"
game_is_done = False


def display_game(row1,row2,row3):

    #game board
    print(row1)
    print(row2)
    print(row3)

def who_starts(players_turn):

    while len(players_turn) == 0:

        players_turn_test = str(input("Which player starts? choices (O/X) "))
        inputcheck = players_turn_test.upper()

        if inputcheck == "X":
            players_turn.append(inputcheck) 
        elif inputcheck == "O":
            players_turn.append(inputcheck)
    print(f"Its the turn off player:  {players_turn} ")

def making_a_move(row1,row2,row3):
    
    move_has_been_made = False
    #checking if the input is accepted
    while move_has_been_made == False:
        accepted_input_1 = False
        accepted_input_2 = False
        
        while accepted_input_1 == False:
        
            choice_row = input("What row would you like to make your move on? [row1,row2,row3] ")
        
            if choice_row == "row1" or choice_row == "row2" or choice_row == "row3":
                accepted_input_1 = True
            else:
                print("Please enter a valid move [row1,row2,row3]")
            
        while accepted_input_2 == False:
            choice_placement = input(f"Where on {choice_row} do you choose? [0,1,2] ")
        
            if choice_placement.isdigit():
                choice_placement_checked = int(choice_placement)
            
                if choice_placement_checked == 0 or choice_placement_checked == 1 or choice_placement_checked == 2:
                    accepted_input_2 = True
                
                else:
                    print("Please enter a valid move [0,1,2]")
                
            else:
                print("Please enter a valid move [0,1,2]")

        if choice_row.lower() == "row1" and row1[choice_placement_checked] == "E":
                
            #updating the game with the players move
            row1[choice_placement_checked] = players_turn[0]
            #display_game(row1,row2,row3)
            move_has_been_made = True
                
        elif choice_row.lower() == "row2" and row2[choice_placement_checked] == "E":    
                
            #updating the game with the players move
            row2[choice_placement_checked] = players_turn[0]
            #display_game(row1,row2,row3)
            move_has_been_made = True
                
        elif choice_row.lower() == "row3" and row3[choice_placement_checked] == "E":

            #updating the game with the players move
            row3[choice_placement_checked] = players_turn[0]
            #display_game(row1,row2,row3)
            move_has_been_made = True
                
                    
        else:
            move_has_been_made = False
            print("That was an invalid move")
            
    if move_has_been_made == True:
        if players_turn[0] == "X":
            players_turn[0] = "O"
                    
        elif players_turn[0] == "O":
            players_turn[0] = "X"
            
    print(f"It's now player: {players_turn[0]}")


def check_if_finished(row1,row2,row3):
    empty = "E"
    marks = ["X", "O"]
    rows = [row1, row2, row3]

    # Checks for victory horizontaly
    for row in rows:
        if row[0] == row[1] and row[0] == row[2] and row[0] != empty:
            return row[0]
            
    # Checks for victory verticaly
    for i in range(3):
        if rows[0][i] == rows[1][i] and rows[0][i] == rows[2][i] and rows[0][i] != empty:
            return rows[0][i]

    for mark in marks:
        if rows[1][1] == mark:
            if rows[0][0] == mark and rows[2    ][2] == mark:
                return mark
            elif rows[2][0] == mark and rows[0][2] == mark:
                return mark

    return ""
    

def play_again():
    pass              
        
def main():
    row1 = ["E","E","E"]
    row2 = ["E","E","E"]
    row3 = ["E","E","E"]
    game_is_done = False
    winner = ""

    while game_is_done == False:

        if game_is_done := bool(check_if_finished(row1,row2,row3)):
            break
        
        #Showing the board
    
        display_game(row1,row2,row3)
        
        #Players choosing who starts
        who_starts(players_turn)
        
        #Checking if one player has won
        
        #player making a move
        making_a_move(row1,row2,row3)

    
    print(f"Congratulations!")
    display_game(row1,row2,row3)

    print("This was the final board")

    #Asking if the player wants to play again.
    play_again = input("Would you like to reset the game? [Y,N] ")
    if play_again.lower() == "y":
        print("Game has now been reset")
        game_is_done = False
        main()
    
    else:
        exit()
    
main()
