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



#LD
#solve_state[:,6]= np.roll(solve_state[:,6], 3, 0)
#solve_state[3:6, 3:6]=np.rot90(solve_state[3:6, 3:6],axes=(1,0))

#LU
#solve_state[:,6]= np.roll(solve_state[:,6], -3, 0)
#solve_state[3:6, 3:6]=np.rot90(solve_state[3:6, 3:6],axes=(0,1))
#only difference is changing the direction and relevant axes

#RU
solve_state[:,8]= np.roll(solve_state[:,8], 3, 0)
solve_state[3:6, 9:12]=np.rot90(solve_state[3:6, 9:12],axes=(1,0))
#only difference is changing the direction and relevant axes

print(solve_state)
#RD
#solve_state[:,8]= np.roll(solve_state[:,8], -3, 0)
#solve_state[3:6, 9:12]=np.rot90(solve_state[3:6, 9:12],axes=(0,1))
#only difference is changing the direction and relevant axes

print(solve_state)