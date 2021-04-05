import random

import matplotlib.pyplot as plt
import numpy as np

from datasets.jester_data import get_jester_data

path = 'datasets/data/jesterfinal151cols.csv'
dataset = get_jester_data(path)

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
plt.hist(jokes_selected)
plt.title('E-greedy: Histogram of jokes selections')
plt.xlabel('Jokes')
plt.ylabel('Number of times each joke was selected')
plt.show()

plt.plot([i for i in range(0, N)], current_reward)
plt.xlabel("Step (s)")
plt.ylabel("Reward")
plt.show()
