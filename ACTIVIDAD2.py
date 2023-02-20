#Juan Sebastian Guzman Franco 
#Maestria en ingeniería cohorte VII 
#Objetivo: Utilizar la serie de Fourier para aproximar la función a trozos o por partes

#Importamos las librerias necesarias 
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal as sp
from sympy import * 
# Importamos las variables simbolicas 'n' y 't'
from sympy.abc import n, t, x

# Periodo
Tmax=3
Tmin=-3
T = Tmax-Tmin
print('el valor del periodo es:',T)

# Frecuencia angular
w = (2*np.pi)/T
print('el valor de la frecuencia angular es:',w)

t = np.arange(-3, 3, 0.01)
squareWaveFunction = np.piecewise(t,[((t>=-T/2) & (t<=-T/4)),((t>-T/4) & (t<T/4)),((t>=T/4) & (t<=T/2))],[-1, 1, -1])


#Graficamos la onda cuadrada
plt.plot(t, squareWaveFunction)
plt.grid()
plt.ylabel('Amplitude')
plt.xlabel('time(t)')
plt.show()

# Integramos la funcion (2/T) cuya variable es 't'
# y limites de integracion son -3 y 3
ao1=0
for i in squareWaveFunction:
    ao = (2/T)*integrate(i, (x, Tmin, Tmax))
    ao1 += ao
print('el valor de ao es:', ao1)    
ao=ao1

an1=0
for i in squareWaveFunction:
    an = (2/T)*integrate(i*(cos(n*w*x)), (x, Tmin, Tmax))
    an1 += an
print('el valor de ao es:', an1)    
an=an1










