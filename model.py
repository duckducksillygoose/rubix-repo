#creating an array
import numpy as np
import random


solve_state = np.empty((9,12), dtype = "str")
solve_state.fill("*")

#make simpler
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

def LD():
    solve_state[:,6]= np.roll(solve_state[:,6], 3, 0)
    solve_state[3:6, 3:6]=np.rot90(solve_state[3:6, 3:6],axes=(1,0))

def LU():
    solve_state[:,6]= np.roll(solve_state[:,6], -3, 0)
    solve_state[3:6, 3:6]=np.rot90(solve_state[3:6, 3:6],axes=(0,1))


def RU():
    solve_state[:,8]= np.roll(solve_state[:,8], 3, 0)
    solve_state[3:6, 9:12]=np.rot90(solve_state[3:6, 9:12],axes=(1,0))



def RD():
    solve_state[:,8]= np.roll(solve_state[:,8], -3, 0)
    solve_state[3:6, 9:12]=np.rot90(solve_state[3:6, 9:12],axes=(0,1))




def TL():
    solve_state[3,:]= np.roll(solve_state[3,:], -3, 0)
    solve_state[0:3, 6:9]=np.rot90(solve_state[0:3, 6:9], axes=(1,0))


def TR():
    solve_state[3,:]= np.roll(solve_state[3,:], 3, 0)
    solve_state[0:3, 6:9]=np.rot90(solve_state[0:3, 6:9], axes=(1,0))


def BL():
    solve_state[5,:]= np.roll(solve_state[5,:], -3, 0)
    solve_state[6:9, 6:9]=np.rot90(solve_state[6:9, 6:9], axes=(0,1))
    

def BR():
    solve_state[5,:]= np.roll(solve_state[5,:], 3, 0)
    solve_state[6:9, 6:9]=np.rot90(solve_state[6:9, 6:9], axes=(0,1))



moves= [TL, TR, BL, BR, LU, LD, RU, RD]


moves_made = []

for i in range(10):
    move = random.choice(moves)
    result = move()
    moves_made.append(move)
    print("selected function is", move)

moves_made = moves_made [::-1]

print(moves_made)

def cube_import():
    print(solve_state)


