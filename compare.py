import matplotlib.pyplot as plt

from datasets.jester_data import get_jester_data

path = 'datasets/data/jesterfinal151cols.csv'
dataset = get_jester_data(path)

# Реализация random selection
import random

N = 24054
d = 150
jokes_selected = []
total_reward = 0
current_reward = [0] * N

for n in range(0, N):
    joke = random.randrange(d)
    jokes_selected.append(joke)
    reward = dataset[n, joke]
    total_reward = total_reward + reward
    current_reward[n] = total_reward

print("Total reward:", total_reward)


plt.plot([i for i in range(0, N)], current_reward, label='Random selection')
plt.xlabel("Step (s)")
plt.ylabel("Reward")

import numpy as np

# Реализация E-greedy
N = 24054
d = 150
jokes_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
current_reward = [0] * N

epsilon = 0.1

for t in range(0, N):
    p = np.random.rand()
    if p > epsilon:
        joke = 0
        max_average_reward = 0
        for i in range(0, d):
            if numbers_of_selections[i] > 0:
                average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            else:
                average_reward = 1e400
            if average_reward > max_average_reward:
                max_average_reward = average_reward
                joke = i
        # np.argmax(self.q[pool_idx])
    else:
        joke = random.randrange(d)

    jokes_selected.append(joke)
    numbers_of_selections[joke] = numbers_of_selections[joke] + 1
    reward = dataset[t, joke]
    sums_of_rewards[joke] = sums_of_rewards[joke] + reward
    total_reward = total_reward + reward
    current_reward[t] = total_reward

# Visualising
plt.plot([i for i in range(0, N)], current_reward, label='E-greedy')
plt.xlabel("Step (s)")
plt.ylabel("Reward")


import math

# Реализация UCB
N = 24054
d = 150
jokes_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
current_reward = [0] * N

for t in range(0, N):
    joke = 0
    max_upper_bound = 0
    for i in range(0, d):
        if numbers_of_selections[i] > 0:
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(2 * math.log(t + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            joke = i
    jokes_selected.append(joke)
    numbers_of_selections[joke] = numbers_of_selections[joke] + 1
    reward = dataset[t, joke]
    sums_of_rewards[joke] = sums_of_rewards[joke] + reward
    total_reward = total_reward + reward
    current_reward[t] = total_reward

# Визуализация результата
plt.plot([i for i in range(0, N)], current_reward, label='UCB')
plt.xlabel("Step (s)")
plt.ylabel("Reward")



# Thomson sampling
N = 24054
d = 150
jokes_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0
current_reward = [0] * N

for t in range(0, N):
    joke = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            joke = i
    jokes_selected.append(joke)
    reward = dataset[t, joke]
    if reward == 1:
        numbers_of_rewards_1[joke] = numbers_of_rewards_1[joke] + 1
    else:
        numbers_of_rewards_0[joke] = numbers_of_rewards_0[joke] + 1

    total_reward = total_reward + reward
    current_reward[t] = total_reward

# Visualising
plt.plot([i for i in range(0, N)], current_reward, label='Thomson sampling')
plt.xlabel("Step (s)")
plt.ylabel("Reward")
plt.legend()
plt.show()

