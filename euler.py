# Written by Ben Pearson
# V 0.3.0
import pandas as pd
import numpy as np

# Initialize constants
L = 1
G = 9.8
ANG_FREQ = np.sqrt(1/9.8)
PI = np.pi
angle = [PI/8, PI/4, 3*PI/8, PI/2]
DT = 0.0200709 # this is T/100 to 6 sig figs

# Arrays to store variables for later use/data analysis
theta = []
omega = [0]
alpha = []

# Incremental Functions
def theta_next(n):
    return DT*omega[n] + theta[n]

def omega_next(n):
    return DT*alpha[n] + omega[n]

def alpha_next(n):
    return - ANG_FREQ**2 * np.sin(theta[n]) 

# Simulation function
def simulate(index, n=200):
    # Add initial values
    theta.append(angle[index])
    alpha.append(alpha_next(0))
    for i in range(n):
        theta.append(theta_next(i))
        omega.append(omega_next(i))
        alpha.append(alpha_next(i))
    # Dump data into CSV file for data analysis
    DF = pd.DataFrame(theta)
    DF.to_csv(r"./data/e_theta_" + str(index) + "_" + str(n) + ".csv")
    DF = pd.DataFrame(omega)
    DF.to_csv(r"./data/e_omega_" + str(index) + "_" + str(n) + ".csv")
    DF = pd.DataFrame(alpha)
    DF.to_csv(r"./data/e_alpha_" + str(index) + "_" + str(n) + ".csv")

