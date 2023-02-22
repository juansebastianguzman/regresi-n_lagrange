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
from sympy.abc import n, t

an1 = (2/T)*integrate(-1*(cos(n*w*t)), (t, -T/2, -T/4))
pprint(an1)  

an2 = (2/T)*integrate(1*(cos(n*w*t)), (t, -T/4, T/4))
pprint(an2) 

an3 = (2/T)*integrate(-1*(cos(n*w*t)), (t, T/4, T/2))
pprint(an3) 

an=an1+an2+an3
print('El valor de an es :', an)

bn1 = (2/T)*integrate(-1*(sin(n*w*t)), (t, -T/2, -T/4))
pprint(bn1)  

bn2 = (2/T)*integrate(1*(sin(n*w*t)), (t, -T/4, T/4))
pprint(bn2) 

bn3 = (2/T)*integrate(-1*(sin(n*w*t)), (t, T/4, T/2))
pprint(bn3) 

bn=bn1+bn2+bn3
print('El valor de bn es :', bn)

print( "f(x) = ")

nCoeficientes = 8
serie = (ao/2)
for i in range(1, nCoeficientes + 1):
    serie = serie + (an*cos(n*w*t)).subs(n, i)
for j in range(1, nCoeficientes + 1):
    serie = serie + (bn*sin(n*w*t)).subs(n, j)

pprint(serie)

t = np.arange(-3, 3, 0.01)

#graficamos las series por separado 

plt.figure()
serie1 = 1.27323954473516*(np.cos(1.0471975511966*t))
plt.plot(t, serie1, 'grey', label = 'serie1')
plt.legend(loc = "lower left")
plt.show()

plt.figure()
serie2 = (1.55926873300775**-16)*np.cos(2.0943951023932*t)
plt.plot(t, serie2, 'grey', label = 'serie2')
plt.legend(loc = "lower left")
plt.show()

plt.figure()
serie3 = - 0.424413181578388*np.cos(3.14159265358979*t)
plt.plot(t, serie3, 'grey', label = 'serie3')
plt.legend(loc = "lower left")
plt.show()

plt.figure()
serie4 = 0.254647908947032*np.cos(5.23598775598299*t)
plt.plot(t, serie4, 'grey', label = 'serie4')
plt.legend(loc = "lower left")
plt.show()

plt.figure()
serie5 = (1.55926873300775**-16)*np.cos(6.28318530717959*t)
plt.plot(t, serie5, 'grey', label = 'serie5')
plt.legend(loc = "lower left")
plt.show()

plt.figure()
serie6 = -0.181891363533595*np.cos(7.33038285837618*t)
plt.plot(t, serie6, 'grey', label = 'serie6')
plt.legend(loc = "lower left")
plt.show()

#grafica serie de furier 

serie1 = 1.27323954473516*(np.cos(1.0471975511966*t))
plt.plot(t, serie1, 'grey', label = 'serie1')

serie2 = (1.55926873300775**-16)*np.cos(2.0943951023932*t)
plt.plot(t, serie2, 'grey', label = 'serie2')

serie3 = - 0.424413181578388*np.cos(3.14159265358979*t)
plt.plot(t, serie3, 'grey', label = 'serie3')

serie4 = 0.254647908947032*np.cos(5.23598775598299*t)
plt.plot(t, serie4, 'grey', label = 'serie4')

serie5 = (1.55926873300775**-16)*np.cos(6.28318530717959*t)
plt.plot(t, serie5, 'grey', label = 'serie5')

serie6 = -0.181891363533595*np.cos(7.33038285837618*t)
plt.plot(t, serie6, 'grey', label = 'serie6')

serieFourier = 1/2 + serie1 + serie2 + serie3 + serie4 + serie5 + serie6 
plt.plot(t, serieFourier, 'orange')
plt.show()

#graficamos la serie con la funcion onda cuadrada 

plt.plot(t, squareWaveFunction, 'black', label = 'f(t)')
etiqueta = 'coeficientes = '+ str(nCoeficientes)
serieFourier =serie1 + serie2 + serie3 + serie4 + serie5 + serie6  
plt.plot(t, serieFourier, 'orange', label = etiqueta)
plt.title('Serie de Fourier')
plt.xlabel('time(t)')
plt.ylabel('Amplitude')
plt.legend(loc = "lower left")
plt.show()