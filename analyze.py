# Written by Ben Pearson
# V0.0.1
# This module is designed to test the conservation of energy in the functions

import numpy as np

# Initialize constants
L = 1
G = 9.8
PI = np.pi
ANGLE = [PI/8, PI/4, 3*PI/8, PI/2]

def test(omega, theta, index):
    ke = L / 2 * omega**2
    pe = G * (np.cos(theta) - np.cos(ANGLE[index]))
    acc_val = - G * L * np.cos(ANGLE[index])
    return (acc_val - (ke + pe)) / acc_val * 100
