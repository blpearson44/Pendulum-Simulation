# Written by Ben Pearson
# V 1.0.0

# Modules
import numpy as np

# Initialize constants
M = 0.5
L = 1.0
G = 9.8
PI = np.pi

# This function recursively calculates the sum in K(x)
def series_sum(x, n=1, total=1, most=3):
    if n > most:
        return total
    else:
        return series_sum(x, n + 1, ((2 * n + 1)/(2 * n + 2))**2 * x**2 * total, most)

# Function to calculate k(x) from the assignment by calling on series_sum
def k(x, most=10):
    total = x**2 / 4
    return PI / 2 * (1 + series_sum(x, 1, total, most))

# Function to calculate period from equation given
def period(angle, most):
    return 4 * (L/G)**(1 / 2) * k(np.sin(angle/2), most)

angle_max = [PI/8, PI/4, 3*PI/8, PI/2]

# Testing purposes
j = 1
for i in angle_max:
    print(j)
    j += 1
    print(period(i, 1))
    print(period(i, 10))
    print(period(i, 100))
    print(period(i, 200))
