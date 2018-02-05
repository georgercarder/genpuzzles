#!/usr/bin/python3

# MIT License
# Copyright (c) 2018 George Carder

import sys
from dlxsudoku import Sudoku
from sudokugridgen import buildAndFinalizeAll
import random


def genPuzzles(rank,difficulty):
    generated = False
    while generated == False:
        P=trypuzzle(rank,difficulty)
        if P!=[] and len(set(P))>=(rank**2):
            generated = True
    return P

def trypuzzle(rank,difficulty):
    B=buildAndFinalizeAll(rank)
    index=list(range(len(B)))
    random.shuffle(index)
    present=int((difficulty/10)*((rank**2)-1)+(1-difficulty/10)*(rank**4))
    blankOrNot = [1]*(present)+[0]*((rank**4)-present)
    generated = False
    grid = B[index[0]]
    gridBlanked = grid[0:rank**4]
    while generated == False:
        random.shuffle(blankOrNot)
        for j in range(rank**4):
            if blankOrNot[j]==0:
                gridBlanked[j] = 0
        gridStringed = ''.join(str(c) for c in gridBlanked)
        s1 = Sudoku(gridStringed)
        try:
            s1.solve()
            if s1.to_oneliner().count('0')==0:
                generated = True
        except:
            sys.stderr = DevNull()
            break 
    return gridBlanked 


class DevNull:
    def write(self, msg):
        pass


sys.stderr = DevNull()
