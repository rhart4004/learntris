#!/usr/bin/env python
import sys

# learntris.py
def printGrid(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[1])):
            print matrix[i][j],
        print

def readGiven():
    matrix = []
    for row in range(0,22):
        matrix.append( raw_input().split() )
    return matrix

def clearGrid(matrix):
    new = []
    for i in range(0,22):
        row = []
        for j in range(0,10):
            row.append('.')
        new.append(row)
    matrix = new
    return matrix

def createITetromino():
    iTetromino = ['c']*4
    blankRow = ['.']*4
    iTetromino = [blankRow, iTetromino, blankRow, blankRow]
    return iTetromino

def createOTetromino():
    oTetromino = ['y']*2
    oTetromino = [oTetromino, oTetromino]
    return oTetromino

def createZTetromino():
    # oTetromino = ['y']*2
    # oTetromino = [oTetromino, oTetromino]
    # return oTetromino
    print "hi"

def clearRow(matrix, rowNum):
    row = []
    for j in range(0,10):
        row.append('.')
    matrix[rowNum] = row
    return matrix

def rowCompleteCheck(matrix):
    complete = []
    for rowNum in range(0, len(matrix)):
        if ('.' not in matrix[rowNum]):
            complete.append(rowNum)
    return complete

matrix = []
matrix = clearGrid(matrix)
score = 0
cleared = 0
while(1):
    command = raw_input()
    if ( command == 'q'):
        sys.exit()
    elif ( command == 'p' ):
        printGrid(matrix)
    elif ( command == 'g' ):
        matrix = readGiven()
    elif ( command == 'c' ):
        matrix = clearGrid(matrix)
    elif ( command == 's' ):
        complete = rowCompleteCheck(matrix)
        for row in complete:
            matrix = clearRow(matrix, row)
            cleared += 1
            score += 100
    elif ( command == '?s' ):
        print score
    elif ( command == 'I' ):
        tetromino = createITetromino()
    elif ( command == 'O' ):
        tetromino = createOTetromino()
    # elif ( command == 'Z' ):
    #     createZTetromino()
    elif ( command == 't' ):
        printGrid(tetromino)
        if ('y' in tetromino[1]):
            print 'hi'
    elif ( command == '?n' ):
        print cleared
    else:
        print "Unknown command"

