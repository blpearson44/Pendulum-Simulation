# Written by Ben Pearson
# V0.5.0
import constants as c
import numpy as np

# Testing function
def test(theta_m, theta, omega):
    lhs = c.L / 2 * omega**2
    rhs = c.G * (np.cos(theta) - np.cos(theta_m))
    return (lhs-rhs) / rhs 
