#!/usr/bin/python3

import re

#win_patern: 8 solution, [[[line],[col]],[[line],[col]],[[line],[col]]]
# wp =    [[[[0],[0]],[[0],[1]],[[0],[2]]],   #first line full
#         [[[0],[0]],[[1],[0]],[[2],[0]]],    #first column full
#         [[[0],[0]],[[1],[1]],[[2],[2]]],    #digonal left top to right bottom
#         [[[0],[1]],[[1],[1]],[[2],[1]]],    #second column full
#         [[[0],[2]],[[2],[2]],[[2],[2]]],    #third column full
#         [[[0],[2]],[[1],[1]],[[2],[0]]],    #digonal right top to left bottom
#         [[[1],[0]],[[1],[1]],[[1],[2]]],    #second line full
#         [[[2],[0]],[[2],[1]],[[2],[2]]],]   #third line full

def set_user():                                         #set name for players
    user =   [input("Player 1 enter your name: "),      #name of player 1
            input("Player 2 enter your name: "),        #name of player 2
            1]                                          #player turn: 1 means O & 2 means X & 0 means someone win & -1 means tie

    return (user)

def set_table():                #init game board
    table =     [["","",""],    #top
                ["","",""],     #mid
                ["","",""]]     #bot

    return (table)

def game_loop(table, user):                                             #interaction with players
    #Choose a line
    line = input("In which line do you want to play ? ")
    if  bool(re.match('^[1-3]*$', line))==True and len(line) == 1:      #verify if in line we found characters 1, 2 or 3 and if length of line equal 1
        line = int(line) - 1                                            #converts line into int and makes minus 1 to have the index
    else:                                                               #if in line we found other characters or the lenght of line is not equal 1, so restart turn
        print("Invalid input, retry")
        return (game_loop(table, user))

    #Choose a column
    col = input("In which column do you want to play ? ")
    if  bool(re.match('^[1-3]*$', col))==True and len(col) == 1:        #verify if in column we found characters 1, 2 or 3 and if length of column equal 1
        col = int(col) - 1                                              #converts column into int and makes minus 1 to have the index
    else:                                                               #if in column we found other characters or the lenght of column is not equal 1, so restart turn
        print("Invalid input, retry")
        return (game_loop(table, user))

    #Verification empty case
    if table[line][col] == "O" or table[line][col] == "X":              #verify if the case who is selected is not free and if that is true restart turn
        print("This case is not empty, retry")
        return (game_loop(table, user))

    return (update_table(table, user, col, line))

def update_table(table, user, col, line):                       #update game board
    if user[2] % 2 == 1:                                        #choose the good character depending on player
        table[line][col] = "O"                                  #1%2=1 so "O"
    else:
        table[line][col] = "X"                                  #2%2=0 so "X"

    print("\n",table[0],"\n",table[1],"\n",table[2],"\n")       #display game board

    return (table)

def game_condition(table, user):                                                        #verify the win or draw and switch or not the player
    for i in range (3):
        if user[2] % 2 == 1:                                                            #choose the good player
            if table[i][0] == "O" and table[i][1] == "O" and table[i][2] == "O":        #verify all line for player 1
                user[2] = 0
            elif table[0][i] == "O" and table[1][i] == "O" and table[2][i] == "O":      #verify all column for player 1
                user[2] = 0
            elif table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O":      #verify digonal left top to right bottom for player 1
                user[2] = 0
            elif table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O":      #verify digonal right top to left bottom for player 1
                user[2] = 0
            if user[2] == 0:
                print(user[0],"wins !")
                return (user)
        else:
            if table[i][0] == "X" and table[i][1] == "X" and table[i][2] == "X":        #verify all line for player 2
                user[2] = 0
            elif table[0][i] == "X" and table[1][i] == "X" and table[2][i] == "X":      #verify all column for player 2
                user[2] = 0
            elif table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X":      #verify digonal left top to right bottom for player 2
                user[2] = 0
            elif table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":      #verify digonal right top to left bottom for player 2
                user[2] = 0
            if user[2] == 0:
                print(user[1],"wins !")
                return (user)

    if "" in table[0] or "" in table[1] or "" in table[2]:                              #verify if the game board is not full
        if user[2] % 2 == 1:
            user[2] = 2
        else:
            user[2] = 1
        return (user)
    else:                                                                               #if the game board is full
        print("Tie!")
        user[2] = -1
        return (user)

if __name__ == "__main__":
    user = set_user()                                           #set name for player
    table = set_table()                                         #init game board
    print("\n",table[0],"\n",table[1],"\n",table[2],"\n")       #display the first game board
    while (True):
        print(user[user[2]-1],"'s turn")                        #display player turn
        table = game_loop(table, user)                          #interaction with players
        user = game_condition(table, user)                      #verify the win or draw and switch or not the player
        if user[2] == 0 or user[2] == -1:                       #if turn equal 0 so the game stop because someone win or if turn equal -1 so the game stop because the game is tie
            break
