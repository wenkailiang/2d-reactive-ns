# main program for testing
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import cantera as ct
import simu2D as sim

# test 1 cell kinetics
# no mesh
# only chemistry

# 1 initialize the problem
input=[0, 0, 0, 0]
mysimu=simu2D(input)

# set up the initial condition
geometry=[1, 1]
mysimu.initial(geometry)

#1D case
N = 100
x = np.linspace(0, 10, N)
u = np.ones(N)

# initial condition
print(x)
for i in range(N):
  print(x[i])
