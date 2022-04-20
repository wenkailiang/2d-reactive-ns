import sys
import numpy as np
import cantera as ct
  
class simu2D:
  def __init__(self):
    self.nx=10
    self.ny=10
    self.Lx=1.0
    self.Ly=1.0
    
  # defined functions
  # initialize the simulation
  def initial(self):
    dx=self.Lx/self.nx
    dy=self.Ly/self.ny
    
  def advance(self, time_end):
  
  def save(self, fname):
    np.savetxt(fname, self.data)
