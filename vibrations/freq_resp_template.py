#
# DML, Feb 2022, Cooper Union
#
#  EOM: m \ddot x + c \dot x + k x = F_0 \cos(\omega t + \Delta)
#
#
# Workshop/homework: add harmonic excitation!

import numpy as np
import matplotlib.pyplot as plt
#from control.matlab import *  # MATLAB-like control toolbox functionality
from scipy.integrate import odeint

# Close all figures
plt.close('all')

# Parameters (SI units)
m = 10
k = 1
c = 0.5

# Driving force spec
wf =  1# driving ang. freq., change to natural frequency for resonance
F0 = 1 # amplitude
delta = 0 # phase offset
f0 = F0/m

# Options integration
x0 = np.array([0, 1]) # IC
T = 100 # integration time
n = 2000 # n steps

# Compute parameters, omega_n, zeta
wn = np.sqrt(k/m)
zeta = c / (2*np.sqrt(k*m))
wd = wn*np.sqrt(1-zeta**2)
gamma = 2*zeta*wn

# EOM: d/dt(q) = f(q) + ...
def eom(q, t):
    """
    Time: t
    State vector: q = [x, v]
    Out: dqdt
    """
    x = q[0]
    v = q[1]

    return [v,
            -k * x / m - c * v / m + f0*np.cos(wf*t + delta)]

# Integrate EOM
t = np.linspace(0, 3*T, 3*n)        # longer time to see steady-state
sol = odeint(eom, x0, t)
x = sol[:, 0]
v = sol[:, 1]

# Plot response
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('x [m]', color=color)
ax1.plot(t, x, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('v [m/s]', color=color)  # we already handled the x-label with ax1
ax2.plot(t, v, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
