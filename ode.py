import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#class ode:
    
# need to change ode
def ode(y, t):
    theta, omega = y
    dydt = [omega, -omega - np.sin(theta)]
    return dydt
    
# define
b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)

sol = odeint(ode, y0, t, args=(b, c))

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
