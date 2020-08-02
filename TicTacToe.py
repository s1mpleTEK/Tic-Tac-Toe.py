#!/bin/usr/python3

import numpy as np

player = 1  #default value
            #1 means O & 2 means X & 0 means someone win

def set_table():
    table = np.zeros((3,3), dtype='i')
    return (table)

def game_loop(table, player):
    return (table)

def win_condition(table, player):
    return  (player)

if __name__ == "__main__":
    print("hello world")
    table = set_table()
    while (True):
        table = game_loop(table, player)
        player = win_condition(table, player)
        if (player == 0):
            break;
