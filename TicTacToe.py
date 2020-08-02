#!/bin/usr/python3

import numpy as np

def set_table():
    table = np.zeros((3,3), dtype='i')
    return (table)

if __name__ == "__main__":
    print("hello world")
    table = set_table()
    print(table)