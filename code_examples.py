import numpy as np

"""
for _ in range(2500):
    number = np.random.rand()
    if number < 0.002775:
        print(number)

for _ in range(round(10 / 0.5)):
    print("Hello")
"""

grid = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
probability_of_decay = 0.5


for index, value in enumerate(grid):
    random_value = np.random.rand()
    if random_value <= probability_of_decay:
        grid[index] = 0

print(grid)



