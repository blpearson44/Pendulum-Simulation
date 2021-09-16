# Written by Ben Pearson
# V0.2.0

# Modules
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

# Increment functions
def theta_next(n, dt):
    return 2 * dt * omega[n] + theta[n-1]

def omega_next(n, dt):
    return 2 * dt * alpha[n] + omega[n-1]

def alpha_next(n):
    return - ANG_FREQ**2 * np.sin(theta[n])

# Simulation Function
def simulate(index, dt, itor):
    # Declare global arrays
    global theta
    global omega
    global alpha
    global error
    # First init
    theta.append(angle[index])
    alpha.append(alpha_next(0))
    error.append(0)
    # Second init
    theta.append(angle[index])
    omega.append(alpha[0]*dt)
    alpha.append(alpha_next(1))
    error.append(0)
    # For the purposes of the program it made more sense to
    # have a third theta generated so the for loop can begin
    # with omega
    theta.append(theta[0] + 2*dt*omega[1])
    for i in range(2, N):
        alpha.append(alpha_next(i))
        omega.append(omega_next(i, dt))
        theta.append(theta_next(i, dt))
        error.append(an.test(omega[i], theta[i], index))
    theta.pop(N)
    # Dump data into csv file for further analysis
    DF = pd.DataFrame([theta, omega, error])
    DF.to_csv(r"./data/lf_" + str(index) + "_" + str(itor) + ".csv")
    # Empty arrays so they can be used again
    theta = []
    omega = [0]
    alpha = []
    error = []
