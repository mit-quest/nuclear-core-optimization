import gym
import statistics
import os
from bwr6x6env import BWR6x6Env

rewards = []
num_iterations = 100000
path_to_config = os.getcwd() + "/configs/bwr6x6_default_config.yaml"
env = BWR6x6Env(path_to_config)
observation = env.reset()

for _ in range(num_iterations):
  action = env.action_space.sample() # this takes random actions
  observation, reward, done, info = env.step(action)

  if done:
    rewards.append(reward)
    observation = env.reset()

env.close()
print("Average reward over {} iterations: {}".format(num_iterations, statistics.mean(rewards)))
