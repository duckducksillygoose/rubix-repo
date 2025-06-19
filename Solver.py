import numpy as np
import random
from model import *


reward = 0 

s_moves=[]
#solution
for i  in range (10):
    step = random.choice(moves)
    s_moves.append(step)
    if s_moves[i] != moves_made[i]:
        reward = reward - 10

    else:
        reward = reward + 1

print(reward)