import numpy as np
import random
from model import *

cube_import()

def flatten_state():
    color_map = {'O': 0, 'B': 1, 'R': 2, 'G': 3, 'Y': 4, 'W': 5, '*': 6}
    flat = solve_state.flatten()
    return np.array([color_map[c] for c in flat])

def is_solved():
    faces = [(3, 0), (3, 3), (3, 6), (3, 9), (0, 6), (6, 6)] #corners of the faces
    for r, c in faces:
        face = solve_state[r:r+3, c:c+3]  # get 3x3 face
        if not np.all(face == face[0, 0]):
            return False
    return True


reward = 0 

s_moves=[]
#solution
for i  in range (10):
    step = random.choice(moves)
    s_moves.append(step)
    if s_moves[i] != moves_made[i]:
        reward = reward - 1

    else:
        reward = reward + 1

print(reward)