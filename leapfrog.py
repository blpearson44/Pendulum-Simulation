# Written by Ben Pearson
# V0.4.0
import pandas as pd
import numpy as np
import constants as c
import period as p
import analyze as an

def simulate(theta_m):
    # Variables to be used in this file
    # Arrays for data
    data = {'theta': [], 'omega': [], 'error': []}

    # First init
    theta = theta_m
    alpha = - c.ANG_FREQ**2 * np.sin(theta)
    omega = 0
    dt = p.period(theta_m, 100) / 100
    data['theta'].append(theta)
    data['omega'].append(omega)
    data['error'].append(0)
    
    # Second init
    theta = theta + omega * dt
    omega = omega + alpha * dt
    alpha = - c.ANG_FREQ**2 * np.sin(theta)
    data['theta'].append(theta)
    data['omega'].append(omega)
    data['error'].append(0)
    
    # For loop to do leap-frog N times
    for i in range(1, c.N):     
        theta = data['theta'][i-1] + 2 * dt * data['omega'][i]
        omega = data['omega'][i-1] + 2 * dt * alpha
        alpha = - c.ANG_FREQ**2 * np.sin(theta)
        # Appending to data dictionary, also for later referal
        data['theta'].append(theta)
        data['omega'].append(omega)
        data['error'].append(an.test(theta_m, theta, omega))
    DF = pd.DataFrame(data)
    DF.to_csv("./data/lf_" + str(theta_m) + ".csv")

# Simulate over each angle
for i in c.ANGLE:
    simulate(i)
