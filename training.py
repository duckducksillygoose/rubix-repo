
from agent import RandomRLAgent
from model import *

solver = RandomRLAgent()

# get to run a certain amount of times
#research more on training
initialise()
scramble()


for ep in range(20):
    reward = solver.run_episode()
    print("Episode", ep+1, "Reward =", reward)