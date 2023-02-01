import numpy as np
import random

# function to get a random number in the range (0,1), not used
#def randomNumber():
#    number = random.uniform(0, 1)
#    while(number == 1) or (number == 0):
#        number = random.uniform(0, 1)
#    return number

# function to create a matrix, dimensions given as arguments
def createMatrix(dimension1, dimension2):
    matrix = np.random.rand(dimension1, dimension2)
    return matrix

# function to multiply matrices, matrices given as arguments
def multiplyMatrices(matrix1, matrix2):
    result = np.matmul(matrix1, matrix2)
    return result

# creating matrices A, B and C
A = createMatrix(pow(10, 6), pow(10, 3))
B = createMatrix(pow(10, 3), pow(10, 6))
C = createMatrix(pow(10, 6), 1)

# multiplying A and B first
AxB = multiplyMatrices(A, B)

# counting D
D = multiplyMatrices(AxB, C)

# printing D
print(D)
