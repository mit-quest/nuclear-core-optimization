import gym
import statistics
import os
from floatenv import FloatEnv

rewards = []
num_iterations = 100000
path_to_config = os.getcwd() + "/configs/float_default_config.yaml"
env = FloatEnv(path_to_config)
observation = env.reset()

for _ in range(num_iterations):
  action = env.action_space.sample() # this takes random actions
  observation, reward, done, info = env.step(action)

  if done:
    rewards.append(reward)
    observation = env.reset()

env.close()
print("Average reward over {} iterations: {}".format(num_iterations, statistics.mean(rewards)))
