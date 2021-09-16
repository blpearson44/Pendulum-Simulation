# Written by Ben Pearson
# V0.0.0
# This program will implement the simulated methods of euler.py and leapfrog.py
# It will then test the results against the criteria of conservation of momentum

# Modules
import leapfrog as lf
import euler as e
import period as p
import numpy as np

# Constants
NUM = [100]
PI = np.pi
ANGLE = [PI/8, PI/4, 3*PI/8, PI/2]

for i in range(4):
    # calculate period for indexed angle 
    period = p.period(i)
    for j in NUM:
       e.simulate(i, period/j, j)
       lf.simulate(i, period/j, j)
