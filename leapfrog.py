# Written by Ben Pearson
# V0.4.0
import pandas as pd
import numpy as np
import constants as c
index = 0

# Variables to be used in this file
# Arrays for data
data = {'theta': [], 'omega': []}
# First init
theta = c.ANGLE[index]
alpha = - c.ANG_FREQ**2 * np.sin(theta)
omega = 0
dt = 0.02
data['theta'].append(theta)
data['omega'].append(omega)

print("Theta\t" + str(theta) + "\t" + "Omega\t" + str(omega))

# Second init
theta = theta + omega * dt
omega = omega + alpha * dt
alpha = - c.ANG_FREQ**2 * np.sin(theta)
data['theta'].append(theta)
data['omega'].append(omega)

for i in range(1, c.N):     
    print("Theta\t" + str(theta) + "\t" + "Omega\t" + str(omega))
    theta = data['theta'][i-1] + 2 * dt * data['omega'][i]
    omega = data['omega'][i-1] + 2 * dt * alpha
    alpha = - c.ANG_FREQ**2 * np.sin(theta)
    data['theta'].append(theta)
    data['omega'].append(omega)


