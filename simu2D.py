import sys
import numpy as np
import cantera as ct

class simu2D:
  
  # initial
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
