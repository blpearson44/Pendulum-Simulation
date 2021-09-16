# Written by Ben Pearson
# V 0.1.0

# Modules
import numpy as np

# Initialize constants
M = 0.5
L = 1.0
G = 9.8
PI = np.pi

# This function recursively calculates the sum in K(x)
def series_sum(x, n=1, total=0.0):
    if n > 3:
        return total
    else:
        return series_sum(x, n + 1, ((2 * n + 1)/(2 * n + 2))**2 * x**2 * total)

# Function to calculate k(x) from the assignment by calling on series_sum
def k(x):
    total = x**2 / 4
    return PI / 2 * (1 + series_sum(x, 1, total))
    
print(k(2))
