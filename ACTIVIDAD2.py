#Juan Sebastian Guzman Franco 
#Maestria en ingeniería cohorte VII 
#Objetivo: Utilizar la serie de Fourier para aproximar la función a trozos o por partes

#Importamos las librerias necesarias 
import numpy as np
import matplotlib.pylab as plt
from scipy import integrate
from scipy import signal as sp
#from sympy import * 
import sympy as sym
# Importamos las variables simbolicas 'n' y 't'
from sympy.abc import n, t

# Periodo
Tmax=3
Tmin=-3
T = Tmax-Tmin
print('el valor del periodo es:',T)

# Frecuencia angular
w = (2*np.pi)/T
print('el valor de la frecuencia angular es:',w)
amplitude = 1


time = np.arange(-3, 3, 0.001)
squareWaveFunction = sym.Piecewise((-1,((t>=-T/2) & (t<=-T/4))))

# Graficamos la onda cuadrada
plt.plot(time, squareWaveFunction, lw=2)
plt.grid()
plt.annotate('T', xy = (np.pi, 0), xytext = (np.pi, -0.01))
plt.annotate('T/2', xy = (np.pi / 2.0, 0), xytext = (np.pi / 2.0, 1.01))
plt.ylabel('Amplitude')
plt.xlabel('time(t)')
plt.show()



