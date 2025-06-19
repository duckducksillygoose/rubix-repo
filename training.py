
from agent import RandomRLAgent

solver = RandomRLAgent()

# get to run a certain amount of times
#research more on training
for ep in range(20):
    reward = solver.run_episode()
    print("Episode", ep+1, "Reward =", reward)