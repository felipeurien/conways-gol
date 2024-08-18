# 1   Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2   Any live cell with two or three live neighbours lives on to the next generation.
# 3   Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4   Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# use "X" for alive and " " for dead 


import os
import time
import random

def createMatrix():

    rows = 40
    columns = 150

    matrix = [[random.randint(0,1) for i in range(columns)] for j in range(rows)]

    for row in matrix:
        print("".join(str(cell) for cell in row))

    return matrix

def countNeighbours(matrix, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows = len(matrix)
    columns = len(matrix[0])
    liveNeighbours = 0

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < rows and 0 <= ny < columns:
            liveNeighbours += matrix[nx][ny]

    return liveNeighbours

def updateMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    newMatrix = [[0 for i in range(columns)] for j in range(rows)]

    for x in range(rows):
        for y in range(columns):
            liveNeighbours = countNeighbours(matrix, x, y)
            if matrix[x][y] == 1:  
                if liveNeighbours in [2, 3]:
                    newMatrix[x][y] = 1  
                else:
                    newMatrix[x][y] = 0  
            else:  
                if liveNeighbours == 3:
                    newMatrix[x][y] = 1  
                else:
                    newMatrix[x][y] = 0  

    return newMatrix

def clearScreen():
    os.system("clear")

def runSimulation():
    matrix = createMatrix()
    
    while True:
        clearScreen()  
        matrix = updateMatrix(matrix)  
        for row in matrix:
            print("".join("█" if cell else " " for cell in row))  
        time.sleep(0.5)  
# █ ■
runSimulation()











#matrixGrl = createMatrix()
#updateMatrix(matrixGrl)


