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

# use rubix cube to visualise how array changes
#Vertical changes: it's not just the column shifting upwards, the back face changes as well
#Horizontal changes = top face does not change, axis loops around by 3

#example of LD manouevre
# solve_state[:,6]=np.roll(solve_state[:,6], 3, 0) 1st step
#O side also needs to be replaced
# something like : solve_state[0:2, 3] = np.roll(solve_state[6,0:2], 


print(solve_state)