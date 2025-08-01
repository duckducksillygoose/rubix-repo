import random
from model import moves, initialise, flatten_state, is_solved, solve_state, scramble

class RandomRLAgent:
    def __init__(self):
        self.history = []
        self.qtable = {}
        self.alpha = 0
        self.gamma = 0
        self.epsilon =0

    def run_episode(self, max_steps=20):
        print("new attempt")
        #scramble 
        total_reward = 0
        choices = []


        for h in range(3):
            choice = random.choice(moves)

            choices.append(choice)
            if is_solved():
                print("Solved!")
                reward = 10
                break
            else:
                reward =-1
        

        

        total_reward += reward
        print(reward)

        # Store: (state, action, reward, new_state)
        state = flatten_state()
        self.history.append((state, reward))



        return total_reward