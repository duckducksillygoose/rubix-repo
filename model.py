#creating an array
import numpy as np
import random


solve_state = np.empty((9,12), dtype = "str")

def initialise():
    for i in range (3,6):
        for j in range (0,3):
            solve_state[i,j] = "O"

    for i in range (3,6):
        for j in range(3,6):
            solve_state[i,j] = "B"
    
    for i in range(3,6):
        for j in range (6,9):
            



initialise()

print(solve_state)