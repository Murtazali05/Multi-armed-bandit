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

plt.hist(jokes_selected)
plt.title('Random Selection: Histogram of jokes selections')
plt.xlabel('Jokes')
plt.ylabel('Number of times each joke was selected')
plt.show()

plt.plot([i for i in range(0, N)], current_reward)
plt.xlabel("Step (s)")
plt.ylabel("Reward")
plt.show()
