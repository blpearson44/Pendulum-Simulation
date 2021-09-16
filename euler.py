# Written by Ben Pearson
# V 0.3.0
import pandas as pd
import numpy as np
import analyze as an

# Initialize constants
L = 1
G = 9.8
ANG_FREQ = np.sqrt(1/9.8)
PI = np.pi
angle = [PI/8, PI/4, 3*PI/8, PI/2]
N = 1000 # max value of n
# Arrays to store variables for later use/data analysis
theta = []
omega = [0]
alpha = []
error = []

# Incremental Functions
def theta_next(n, dt):
    return dt*omega[n] + theta[n]

def omega_next(n, dt):
    return dt*alpha[n] + omega[n]

def alpha_next(n):
    return - ANG_FREQ**2 * np.sin(theta[n]) 

# Simulation function
def simulate(index, dt, itor):
    # Add initial values
    theta.append(angle[index])
    alpha.append(alpha_next(0))
    for i in range(N):
        theta.append(theta_next(i, dt))
        omega.append(omega_next(i, dt))
        alpha.append(alpha_next(i))
        error.append(an.test(theta[i], omega[i], index))
    # Dump data into CSV file for data analysis
    DF = pd.DataFrame([theta, omega, error])
    DF.to_csv(r"./data/e_" + str(index) + "_" + str(itor) + ".csv")
