#Tic Tac Toe game assigment from udemy course:
#By Sondre Fagerhus
#Date 7/5/2022


#Creating the board

row1 = ["E","E","E"]
row2 = ["E","E","E"]
row3 = ["E","E","E"]

row1_instruction = ["1","2","3"]
row2_instruction = ["4","5","6"]
row3_instruction = ["7","8","9"]


winner = ""

players_turn = []

player1 = "X"
player2 = "O"
game_is_done = False


def instruction():

    #printing which number corresponds to which field on the board
    print(f" row1: {row1_instruction}")
    print(f" row1: {row2_instruction}")
    print(f" row1: {row3_instruction}")


def display_game(row1,row2,row3):

    #game board
    print(f" row1: {row1}")
    print(f" row2: {row2}")
    print(f" row3: {row3}")

def who_starts(players_turn):

    while len(players_turn) == 0:

        players_turn_test = str(input("Which player starts? choices (O/X) "))
        inputcheck = players_turn_test.upper()

        if inputcheck == "X":
            players_turn.append(inputcheck) 
        elif inputcheck == "O":
            players_turn.append(inputcheck)
        print(f"Its the turn off player:  {players_turn} ")

def making_a_move(row1,row2,row3,players_turn):

    row_check = row1 + row2 + row3
    if "E" not in row_check:
        print("No legal moves, the game ends in a draw")
        play_again()
    else:
        pass
                            
    
    move_has_been_made = False
    #checking if the input is accepted
    while move_has_been_made == False:
        accepted_input_2 = False
            
        while accepted_input_2 == False:
            choice_placement = input(f"Where on the board do you choose? row1: [1,2,3] row2: [4,5,6] row3: [7,8,9]")

            if choice_placement.isdigit():

                choice_placement_int = int(choice_placement)
            
                if choice_placement_int in (range(1,10)):
                    choice_placement_checked = int(choice_placement)
                    choice_placement_checked = choice_placement_checked - 1

                    if choice_placement_checked in range(0,3):
                        if row1[choice_placement_checked] == "E":
                            row1[choice_placement_checked] = players_turn[0]
                            move_has_been_made = True
                            accepted_input_2 = True
                        else:
                            print("Invalid position chosen, please choose another position")
                            pass

                    elif choice_placement_checked in range(3,6):
                        choice_placement_checked = choice_placement_checked - 3
                        if row2[choice_placement_checked] == "E":
                            
                            row2[choice_placement_checked] = players_turn[0]
                            move_has_been_made = True
                            accepted_input_2 = True
                        else:
                            print("Invalid position chosen, please choose another position")
                            pass

                    elif choice_placement_checked in range(6,9):
                        choice_placement_checked = choice_placement_checked - 6
                        if row3[choice_placement_checked] == "E":
                            
                            row3[choice_placement_checked] = players_turn[0]
                            move_has_been_made = True
                            accepted_input_2 = True
                        else:
                            print("Invalid position chosen, please choose another position")
                            pass
                    else:
                        pass


    
                else:
                    print("Please enter a valid move row1: [1,2,3] row2: [4,5,6] row3: [7,8,9]")


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


    # Checks for victory horizontally
    for row in rows:
        if row[0] == row[1] and row[0] == row[2] and row[0] != empty:
            return row[0]
            
    # Checks for victory vertically
    for i in range(3):
        if rows[0][i] == rows[1][i] and rows[0][i] == rows[2][i] and rows[0][i] != empty:
            return rows[0][i]

    for mark in marks:
        if rows[1][1] == mark:
            if rows[0][0] == mark and rows[2    ][2] == mark:
                return mark
            elif rows[2][0] == mark and rows[0][2] == mark:
                return mark

    if empty in rows == False:
        even_check = "even"
        return even_check
        

    return ""
    
def play_again():

    play_again = input("Would you like to reset the game? [Y,N] ")
    if play_again.lower() == "y":
        print("Game has now been reset")
        main()
    
    else:
        exit()    
        
def main():
    instruction()
    row1 = ["E","E","E"]
    row2 = ["E","E","E"]
    row3 = ["E","E","E"]
    game_is_done = False
    even_check = ""

    while game_is_done == False:

        #Players choosing who starts

        #who_starts(players_turn)
        #Displaying current board

        #This checks if the game is finished
        if game_is_done := bool(check_if_finished(row1,row2,row3)):
            test = check_if_finished(row1,row2,row3)
            print(test)
            break
        elif even_check == "even":
            game_is_done = False
            print("Even")
            print("The game ended in an even:")
            #play_again()
        else:
            pass


        who_starts(players_turn)
        #Displaying current board

        
        #player making a move
        making_a_move(row1,row2,row3,players_turn)

        display_game(row1,row2,row3)

    
    print(f"Congratulations! {test}")

    display_game(row1,row2,row3)

    print("This was the final board")
    print(f"Congratulations! {test}")
main()
