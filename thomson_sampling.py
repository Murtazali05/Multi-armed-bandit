import random

import matplotlib.pyplot as plt

from datasets.jester_data import get_jester_data

path = 'datasets/data/jesterfinal151cols.csv'
dataset = get_jester_data(path)

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
plt.hist(jokes_selected)
plt.title('Thomson Sampling: Histogram of jokes selections')
plt.xlabel('Jokes')
plt.ylabel('Number of times each joke was selected')
plt.show()


plt.plot([i for i in range(0, N)], current_reward)
plt.xlabel("Step (s)")
plt.ylabel("Reward")
plt.show()