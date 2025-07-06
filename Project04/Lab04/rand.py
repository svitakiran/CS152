"""
Svita Kiran
Fall 23
CS 152
10/04/05

python3 rand.py

"""

import random
import matplotlib.pyplot as plt

def gen_random(N):
    numbers = []
    i = 0
    while (i < N):
        i += 1
        x = random.random()
        numbers.append(x)
    return numbers

def genNintegers(num_points, lowerBound, upperBound):
    numbers = []
    i = 0
    while (i < num_points):
        i += 1
        x = random.randint(lowerBound,upperBound)
        numbers.append(x)
    return numbers

def genNnormal(N, mean, std):
    numbers = []
    i = 0
    while (i < N):
        i += 1
        x = random.gauss(mean, std)
        numbers.append(x)
    return numbers

def test():
    x = (gen_random(10))
    y = (genNintegers(10, -10, 10))
    z = (genNnormal(10, 0, 0.2))
    
    plt.plot(x, z, 'o')
    plt.title("Random Numbers")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()
test()