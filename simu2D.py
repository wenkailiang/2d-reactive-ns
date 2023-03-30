import sys
import numpy as np
import cantera as ct
import matplotlib.pyplot as plt

# define the class
class simu2D:
  
  # initialize the simulation
  def __init__(self):
    self.nx=10
    self.ny=10
    self.Lx=1.0
    self.Ly=1.0
    
  # defined functions
  def advance(self, time_end):
  
  def save(self, fname):
    np.savetxt(fname, self.data)
    
  def central1(self):
    cells = np.linspace(0, 1, 0.0001)
    
  def upwind1(self):
    
  def onestep(self):
    
  def rate(a, n, Ea, R, T):
    return a*T^n*np.exp(Ea/R/T)
  def rate1(a, n, Ea, T):
    R = 8.31 # gas constant
    return a*T^n*np.exp(Ea/R/T)
