# Written by Ben Pearson
# V0.4.0
import pandas as pd
import numpy as np
import constants as c
index = 0

# Data dictionary
data = {'theta': [], 'omega': []}
# Variables to be used in this file
theta = c.ANGLE[index]
alpha = - c.ANG_FREQ**2 * np.sin(theta)
omega = 0
dt = 0.02
data['theta'].append(theta)
data['omega'].append(omega)
for i in range(c.N):
    print("Theta\t" + str(theta) + "\t" + "Omega\t" + str(omega))
    theta = theta + omega * dt
    omega = omega + dt * alpha
    alpha = - c.ANG_FREQ**2 * np.sin(theta)
    data['theta'].append(theta)
    data['omega'].append(omega)
