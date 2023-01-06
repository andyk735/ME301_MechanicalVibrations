from control.matlab import tf, bode
import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import odeint

#
# DML, Feb 2022, Cooper Union
#  Bode plot of mass-spring damper system, see Inman Fig. 2.8
#   NOTE: u is input (base excitation),
#   NOTE: y is output (displacement mass).
 #  EOM: m \ddot y + c \dot y + k y =  c \dot u + k u
#  or,    \ddot y + 2*\zeta*\omega_n \dot y + \omega_n^2 y = \
#                   2*\zeta*\omega_n \dot u + \omega_n^2 u
#
#

# Close all figures
plt.close('all')
s = tf('s')

# Parameters
delta = 0
c = 20*(10^2)
k = 4*(10^2)
m = 1007
zeta = c/(2*np.sqrt(k*m))
zetas = [zeta]

omegan = 1
r = np.linspace(0, 2, 100)
omega = r * omegan

plt.figure()
fig, ax = plt.subplots(2)
for zeta in zetas:
    Gn =  (2*zeta*omegan*s + omegan**2) / (s**2 + 2*zeta*omegan*s + omegan**2) # normalized TF
    mag, phase, omega = bode(Gn, omega, plot=False)
    # Plot response
    ax[0].plot(r, mag, label=r'$\zeta=$'+' {}'.format(zeta))
    ax[1].plot(r, phase, label=r'$\zeta=$'+' {}'.format(zeta))


ax[0].set_ylabel(r'Displacement ratio $Y \,/\, U$')
ax[0].set_ylim(0, 6)
ax[0].plot([0, np.sqrt(2)], [1, 1], 'k--')
ax[0].plot([np.sqrt(2), np.sqrt(2)], [0, 1], 'k--')

ax[1].set_ylabel(r'Phase')
ax[0].legend()
ax[1].legend()
ax[1].set_xlabel(r'$r = \omega/\omega_n$')

# Include Y vs V

plt.show()