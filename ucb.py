import math

import matplotlib.pyplot as plt

from datasets.jester_data import get_jester_data

path = 'datasets/data/jesterfinal151cols.csv'
dataset = get_jester_data(path)

# Реализация UCB
N = 24054
d = 150
jokes_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0

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

# Визуализация результатов
plt.hist(jokes_selected)
plt.title('UCB: Histogram of jokes selections')
plt.xlabel('Jokes')
plt.ylabel('Number of times each joke was selected')
plt.show()
