#creating an array
import numpy as np
import random


solve_state = np.empty((9,12), dtype = "str")
solve_state.fill("*")


def initialise():
    for i in range (3,6):
        for j in range (0,3):
            solve_state[i,j] = "O"
        for k in range (3,6):
            solve_state[i,k] = "B"
        for l in range (6,9):
            solve_state[i,l] = "R"
        for m in range (9,12):
            solve_state[i,m] = "G"
    
    for i in range (6,9):
        for j in range(0,3):
            solve_state[j,i] = "Y"
        
        for k in range(6,9):
            solve_state[i,k] = "W"
    
    print(solve_state)


initialise()

print("NEW ARRAY")

solve_state[:,6] = np.roll(solve_state[:,6], shift = 3, axis = 0)
print(solve_state)