#Juan Sebastian Guzman Franco 
#Maestria en ingeniería cohorte VII 
#Objetivo: Utilizar la serie de Fourier para aproximar la función a trozos o por partes

#Importamos las librerias necesarias 
import numpy as np
import matplotlib.pyplot as plt
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


time = np.linspace(-3, 3)
squareWaveFunction = np.piecewise(time,[((time>=-T/2) & (time<=-T/4)),((time>-T/4) & (time<T/4)),((time>=T/4) & (time<=T/2))],[-1, 1, -1])
print(squareWaveFunction)

#Graficamos la onda cuadrada
plt.plot(time, squareWaveFunction)
plt.grid()
plt.ylabel('Amplitude')
plt.xlabel('time(t)')
plt.show()



