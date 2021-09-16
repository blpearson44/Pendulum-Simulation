# Written by Ben Pearson
# V 1.1.1

# Modules
import numpy as np
import constants as c

# This function recursively calculates the sum in K(x)
def series_sum(x, n, total, most):
    if n > most:
        return total
    else:
        return series_sum(x, n + 1, ((2 * n + 1)/(2 * n + 2))**2 * x**2 * total, most)

# Function to calculate k(x) from the assignment by calling on series_sum
def k(x, most=10):
    # Set a_1
    total = x**2 / 4
    return c.PI / 2 * (1 + series_sum(x, 1, total, most))

# Function to calculate period from equation given
def period(index, most=c.N):
    return 4 * np.sqrt(c.L/c.G) * k(np.sin(c.ANGLE[index]/2), most)

