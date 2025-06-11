# Create a function that returns a list of 100 randomly generated numbers.

import random
# Write your function here.
def rng(lst):
    return [random.randint(1, 100) for _ in range(100)]

print(rng([]))