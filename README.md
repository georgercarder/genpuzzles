# genpuzzles.py and puzzleToDataBase.py

genpuzzles.py generates sudoku puzzles of a given rank and difficulty
puzzleToDataBase.py is a script to stock database with such puzzles

genpuzzles.py calls modules sudokugridgen (my own) and dlxsudoku. 
dlxsudoku is a great tool to test whethera candidate sudoku puzzle is valid.

##Use:

To stock a Mongo database with qty puzzles of a particular rank and difficulty
in python3 shell call

`from puzzleToDataBase import *`

`B=buildAndFinalizeAll(rank)` or `B=buildAndFinalizeAllLimit(rank,L)`
`putInDb(rank, difficulty, qty, B)`
