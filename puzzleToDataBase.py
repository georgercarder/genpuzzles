#!/usr/bin/python3

# MIT License
# Copyright (c) 2018 George Carder

from pymongo import MongoClient
from genpuzzles import *
from sudokugridgen import *

# We build a database of Sudoku Puzzles

client = MongoClient('mongodb://localhost:27017')

db = client.SudokuDb

puzzles = db.puzzles

<<<<<<< HEAD
#B=buildAndFinalizeAll(rank)

def putInDb(rank, difficulty, qty, B):
=======
def putInDb(rank,difficulty,qty):
    #here put buildAndFinalize(rank)  take out of genpuzz..
    B=buildAndFinalizeAll(rank) 
>>>>>>> f8f2e9ea056836fc7f20a3307f207406d90adf44
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





