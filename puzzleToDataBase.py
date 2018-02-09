#!/usr/bin/python3

# MIT License
# Copyright (c) 2018 George Carder

from pymongo import MongoClient
from genpuzzles import *

# We build a database of Sudoku Puzzles

client = MongoClient('mongodb://localhost:27017')

db = client.SudokuDb

puzzles = db.puzzles

#B=buildAndFinalizeAll(rank)

def putInDb(rank, difficulty, qty, B):
    for i in range(qty):
        entered = False
        while entered == False:
            puzz = genPuzzles(rank,difficulty,B)
            if type(puzzles.find_one({'puzzle': puzz}))!=dict:
                post = {
                    'rank' : rank,
                    'difficulty' : difficulty,
                    'puzzle' : puzz 
                }
                new_result = puzzles.insert_one( post )
                print(" {} inserted".format(new_result.inserted_id))
                entered = True
            else:
                print('duplicate')
    list(puzzles.find())





