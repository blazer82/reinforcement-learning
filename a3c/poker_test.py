import gym

import sys
sys.path.append('../gym-pypoker')
import gym_pypoker

env = gym.make("PyPoker-v0")

# Episode
print(env.action_space)
env.reset()
observation, reward, episode_over, info = env.step(0)

print(observation)