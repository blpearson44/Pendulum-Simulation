# Written by Ben Pearson
# V0.4.0
import pandas as pd
import numpy as np
import constants as c
import period as p
import analyze as an

def simulate(theta_m):
    # Data dictionary
    data = {'theta': [], 'omega': [], 'error': []}
    # Variables to be used in this file
    theta = theta_m
    alpha = - c.ANG_FREQ**2 * np.sin(theta)
    omega = 0
    dt = p.period(theta_m, 100) / 100
    data['theta'].append(theta)
    data['omega'].append(omega)
    data['error'].append(0)
    # implement euler's method
    for i in range(1, c.N):
        theta = theta + omega * dt
        omega = omega + dt * alpha
        alpha = - c.ANG_FREQ**2 * np.sin(theta)
        data['theta'].append(theta)
        data['omega'].append(omega)
        data['error'].append(an.test(theta_m, theta, omega))
    DF = pd.DataFrame(data)
    DF.to_csv("./data/e_" + str(theta_m) + ".csv")

for i in c.ANGLE:
    simulate(i)
