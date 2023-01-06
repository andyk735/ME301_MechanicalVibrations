from control.matlab import tf
import matplotlib.pyplot as plt
import numpy as np
#from scipy.integrate import odeint

#
# DML, Feb 2022, Cooper Union
#  Bode plot of mass-spring damper system, see Inman Fig. 2.14
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
v = np.linspace(0,150,1000) # % km/hr
v = v / 3.6 # m/s
wave_length = 6 # wavelength road in m
U = 0.01 # road amplitude in m
m = 1007
k = 4e4
c = 20e2 # SI units
m = 1585

# Convert to standard form
omegan = np.sqrt(k/m)
omega = 2 * np.pi * v / wave_length
zeta = c / (2 * m * omegan)

# Plot range of driving freq. for given wavelength and speeds
plt.figure()
plt.plot(v*3.6, omega/(2*np.pi))
plt.xlabel('v [km/hr]')
plt.ylabel('f [Hz]')

# Displacement transmissibility: Magnitude, Phase plot
r = omega / omegan

# Magnitude
M = np.sqrt((1+ (2 * zeta * r)**2) / ((1 - r**2)**2 + (2 * zeta * r)**2))
# Displacement of Car
Y = U * M        # output amplitude Y obtained by multiplying by input amplitude U

plt.figure()
plt.plot(v*3.6,Y*100)
plt.xlabel('v [km/hr]')
plt.ylabel('X [cm]')
plt.title('Displacement transmissibility')

# Force transmissibility: Magnitude, Phase plot
Fn = r**2 * M
F = k * U * Fn

plt.figure()
plt.plot(v*3.6,F)
plt.xlabel('v [km/hr]')
plt.ylabel('F [N]')
plt.title('Force transmissibility')

plt.figure()
plt.plot(v*3.6,F/m)
plt.xlabel('v [km/hr]')
plt.ylabel('a (vertical) [m/s^2]')

plt.show()
