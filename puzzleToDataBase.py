#!/usr/bin/python3

# MIT License
# Copyright (c) 2018 George Carder

from pymongo import MongoClient
from genpuzzles import *

# We build a database of Sudoku Puzzles

client = MongoClient('mongodb://localhost:27017')

db = client.SudokuDb

puzzles = db.puzzles

def putInDb(rank,difficulty,qty):
    for i in range(qty):
        post = {
                'rank' : rank,
                'difficulty' : difficulty,
                'puzzle' : genPuzzles(rank,difficulty)
                }
        new_result = puzzles.insert_one( post )
        print(" {} inserted".format(new_result.inserted_id))
    list(puzzles.find())





