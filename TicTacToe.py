#!/usr/bin/python3

import numpy as np

player = 1  #default value
            #1 means O & 2 means X & 0 means someone win

def set_usr():
    usr =   [input("Player 1 enter your name: "),
            input("Player 2 enter your name: "),
            player]
    return (usr)

def set_table():
    table = np.zeros((3,3), dtype='i')
    return (table)

def game_loop(table, usr):
    return (table)

def win_condition(table, usr):
    return (usr)

if __name__ == "__main__":
    usr = set_usr()
    table = set_table()
    while (True):
        table = game_loop(table, usr)
        usr = win_condition(table, usr)
        if (usr[2] == 0):
            break
