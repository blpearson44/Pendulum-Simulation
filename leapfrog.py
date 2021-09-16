# Written by Ben Pearson
# V0.2.0

# Modules
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

# Increment functions
def theta_next(n):
    return 2 * DT * omega[n] + theta[n-1]

def omega_next(n):
    return 2 * DT * alpha[n] + omega[n-1]

def alpha_next(n):
    return - ANG_FREQ**2 * np.sin(theta[n])

# Simulation Function
def simulate(index, n=200):
    # First init
    theta.append(angle[index])
    alpha.append(alpha_next(0))
    # Second init
    theta.append(angle[index])
    omega.append(alpha[0]*DT)
    alpha.append(alpha_next(1))
    # For the purposes of the program it made more sense to
    # have a third theta generated so the for loop can begin
    # with omega
    theta.append(theta[0] + 2*DT*omega[1])
    for i in range(2, n):
        alpha.append(alpha_next(i))
        omega.append(omega_next(i))
        theta.append(theta_next(i))
    # Dump data into csv file for further analysis
    DF = pd.DataFrame(theta)
    DF.to_csv(r"./data/lf_theta_" + str(index) + "_" + str(n) + ".csv")
    DF = pd.DataFrame(omega)
    DF.to_csv(r"./data/lf_omega_" + str(index) + "_" + str(n) + ".csv")
    DF = pd.DataFrame(alpha)
    DF.to_csv(r"./data/lf_alpha_" + str(index) + "_" + str(n) + ".csv")









