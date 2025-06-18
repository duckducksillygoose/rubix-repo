import random
from model import moves, initialise, encode_state, is_solved, solve_state

class RandomRLAgent:
    def __init__(self):
        self.history = []

    def run_episode(self, max_steps=20):
        initialise()  # reset cube
        total_reward = 0

        for step in range(max_steps):
            action_index = random.randint(0, len(moves) - 1)
            move = moves[action_index]
            move()  # apply move

            reward = 10 if is_solved() else -1
            total_reward += reward

            # Store: (state, action, reward, new_state)
            state = encode_state()
            self.history.append((state, action_index, reward))

            if is_solved():
                print(f"Solved in {step + 1} steps!")
                break

        return total_reward