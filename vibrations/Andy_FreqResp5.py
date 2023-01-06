#
# Andy Kim, Homework 2 Question 5
#
#

import numpy as np
import matplotlib.pyplot as plt
#from control.matlab import   # MATLAB-like control toolbox functionality
from scipy.integrate import odeint

# Close all figures
plt.close('all')

# Parameters (SI units)
a = 1
x0 = 1
Fw = 1
g = 9.8

m = a*(x0**-1.4)/g
xi = 1.5            # Large Oscillation Release Point

x1 = np.linspace(0.98, 1.02, 100)

# Force
F_net = a*(x1**-1.4) - a*(x0**-1.4)
F_netsmall = -1.4*a*(x0**-2.4)*(x1-x0)

# EOM: d/dt(q) = f(q) + ...
def eom(q, t):
    """
    Time: t
    State vector: q = [x, v]
    Out: dqdt
    """
    x = q[0]
    v = q[1]

    return [v, (a/m)*((x**-1.4) - (x0**-1.4))]

# Integrate EOM
t = np.linspace(0, 10, 300)
sol = odeint(eom, [xi, 0], t)
x = sol[:, 0]
v = sol[:, 1]

# Plot response
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Displacement [m]')
ax1.set_ylabel('Net Force [N]', color=color)
ax1.plot(x1, F_net, color=color, label='F_net')
ax1.plot(x1, F_netsmall, color='b', label='F_net Approx')
ax1.tick_params(axis='y', labelcolor=color)
plt.legend(loc="upper right")

fig2, ax2 = plt.subplots()
color = 'tab:red'
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Displacement [m]', color=color)  # we already handled the x-label with ax1
ax2.plot(t, x, color=color, label='Displacement')
ax2.tick_params(axis='y', labelcolor=color)

ax3 = ax2.twinx()
color = 'tab:blue'
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Velocity [m]', color=color)  # we already handled the x-label with ax1
ax3.plot(t, v, color=color, label='Velocity')
ax3.tick_params(axis='y', labelcolor=color)

fig2.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()