#Juan Sebastian Guzman Franco 
#Maestria en ingeniería cohorte VII 
#Objetivo: Utilizar la serie de Fourier para aproximar la función a trozos o por partes

#Importamos las librerias necesarias 
import numpy as np
import matplotlib.pylab as plt
from scipy import signal as sp

# Importamos todo el modulo sympy
from sympy import *

# Importamos las variables simbolicas 'n' y 't'
from sympy.abc import n, t

# Periodo
#T = pi

# Frecuencia angular
w = (2*pi)/T
amplitude = 1
time = np.arange(-1, 10, 0.001)
squareWaveFunction = (sp.square(2*time) * amplitude/2.0) + amplitude/2.0

# Graficamos la onda cuadrada
plt.plot(time, squareWaveFunction, lw=2)
plt.grid()
plt.annotate('T', xy = (np.pi, 0), xytext = (np.pi, -0.01))
plt.annotate('T/2', xy = (np.pi / 2.0, 0), xytext = (np.pi / 2.0, 1.01))
plt.ylabel('Amplitude')
plt.xlabel('time(t)')


# Integramos la funcion (2/T) cuya variable es 't'
# y limites de integracion son 0 y pi/2

ao = 2/T*integrate(1, (t, 0, T/2))

print("a0 = ")
pprint(ao)

# Integramos la funcion (2/pi)*cos(2nt) 
# Su variable es 't' y sus limites de integracion son 0 y pi/2
an = (2/T)*integrate(cos(n*w*t), (t, 0, T/2))

print("an = ")
pprint(an)

# Integramos la funcion (2/pi*sin(2nt)
# Su variable es 't' y sus limites de integracion son 0 y pi/2. 
bn = (2/T)*integrate(sin(n*w*t), (t, 0, T/2))

print("bn = ")
pprint(bn)
