import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import cantera as ct
import simu2D as sim


# test problem
# 2D shock

# 1 initialize the problem
input=[0, 0, 0, 0]
mysimu=simu2D(input)

# set up the initial condition
geometry=[1, 1]
mysimu.initial(geometry)

grid = np.arange(0, 10, 0.01)
print(grid)
