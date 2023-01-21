#Juan Sebastian Guzman Franco 
#Maestria en ingeniería cohorte VII 
#Objetivo: Desarrollar un codigo utilizando interpolaciones vistas en clase que me permita determinar 
#las dimensiones de un mecanismo para un segmento rectilíneo de 20 cm, con un rango angular de 55
#grados de giro de la manivela para un mecanismo 4 barras de Hoeken, teniendo en cuenta los criterios 
#de optimización de rectitud y velocidad.

#Importamos las librerias necesarias 

from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt

# interpolación lagrange

#Valores de entrada
val1=int(input("ingrese el valor delta_beta solicitado: "))
val2=int(input("Ingrese el valor delta_x que solicitado: "))

# Guardamos los valores de x y f(x) a usar, en vectores, teniendo en cuenta que estos valores son para 
#optimización por rectitud.
x = [20,40,60,80,100,120,140,160,180]
#y1 es la relacion delta_x/L2
y1 = [0.601,1.193,1.763,2.299,2.790,3.238,3.623,3.933,4.181]
#y2 es la relacion L3/L2
y2 = [3.963,3.925,3.850,3.738,3.588,3.438,3.250,3.025,2.800]
#y3 es la relacion L1/L2
y3 = [2.975,2.950,2.900,2.825,2.725,2.625,2.500,2.350,2.200]

# Obtenemos el polinomio de Lagrange para los puntos dados
p1 = lagrange(x,y1)
p2 = lagrange(x,y2)
p3 = lagrange(x,y3)

#Los resultados de las relaciones son:
rel1=float(p1(val1))
rel2=float(p2(val1))
rel3=float(p3(val1))

print(f"Los resultados obtenidos mediante la interpolación de lagrange son:")

#print(f"la relación delta_x/L2 es: {rel1}")
#print(f"la relación L3/L2 es: {rel2}")
#print(f"la relación L1/L2 es: {rel3}")

#Los resultados de la longitud de los eslabones son 
L2=float(val2/rel1)
L3=float(rel2*L2)
L1=float(rel3*L2)

print(f'La longitud de los eslabones para optimización de rectitud son:')
print(f"La longitud del eslabon L1 es: {L1}")
print(f"La longitud del eslabon L2 es: {L2}")
print(f"La longitud del eslabon L3 es: {L3}")

# Guardamos los valores de f(x) a usar, en vectores, teniendo en cuenta que estos valores son para optimización
#por velocidad.
#y4 es la relacion delta_x/L2
y4 = [0.480,0.950,1.411,1.845,2.237,2.600,2.932,3.232,3.456]
#y5 es la relacion L3/L2
y5 = [2.613,2.575,2.538,2.463,2.350,2.238,2.125,2.013,1.863]
#y6 es la relacion L1/L2
y6 = [2.075,2.050,2.025,1.975,1.900,1.825,1.750,1.675,1.575]

# Obtenemos el polinomio de Lagrange para los puntos dados
p4 = lagrange(x,y4)
p5 = lagrange(x,y5)
p6 = lagrange(x,y6)

#Los resultados de las relaciones son:
rel4=float(p4(val1))
rel5=float(p5(val1))
rel6=float(p6(val1))

#print(f"la relación delta_x/L2 es: {rel4}")
#print(f"la relación L3/L2 es: {rel5}")
#print(f"la relación L1/L2 es: {rel6}")

#Los resultados de la longitud de los eslabones son 
L5=float(val2/rel4)
L6=float(rel5*L5)
L4=float(rel6*L5)

print(f'La longitud de los eslabones para optimización de velocidad son:')
print(f"La longitud del eslabon L1 es: {L4}")
print(f"La longitud del eslabon L2 es: {L5}")
print(f"La longitud del eslabon L3 es: {L6}")


# interpolación linear

if val1>x[0] and val1<x[1]:
    rel7=float(y1[0]+((y1[1]-y1[0])*(val1-x[0])/(x[1]-x[0])))
    rel8=float(y2[0]+((y2[1]-y2[0])*(val1-x[0])/(x[1]-x[0])))
    rel9=float(y3[0]+((y3[1]-y3[0])*(val1-x[0])/(x[1]-x[0])))
    rel10=float(y4[0]+((y4[1]-y4[0])*(val1-x[0])/(x[1]-x[0])))
    rel11=float(y5[0]+((y5[1]-y5[0])*(val1-x[0])/(x[1]-x[0])))
    rel12=float(y6[0]+((y6[1]-y6[0])*(val1-x[0])/(x[1]-x[0])))
    
elif val1>x[1] and val1<x[2]:
    rel7=float(y1[1]+((y1[2]-y1[1])*(val1-x[1])/(x[2]-x[1])))
    rel8=float(y2[1]+((y2[2]-y2[1])*(val1-x[1])/(x[2]-x[1])))
    rel9=float(y3[1]+((y3[2]-y3[1])*(val1-x[1])/(x[2]-x[1])))
    rel10=float(y4[1]+((y4[2]-y4[1])*(val1-x[1])/(x[2]-x[1])))
    rel11=float(y5[1]+((y5[2]-y5[1])*(val1-x[1])/(x[2]-x[1])))
    rel12=float(y6[1]+((y6[2]-y6[1])*(val1-x[1])/(x[2]-x[1])))
   
elif val1>x[2] and val1<x[3]:
    rel7=float(y1[2]+((y1[3]-y1[2])*(val1-x[2])/(x[3]-x[2])))
    rel8=float(y2[2]+((y2[3]-y2[2])*(val1-x[2])/(x[3]-x[2])))
    rel9=float(y3[2]+((y3[3]-y3[2])*(val1-x[2])/(x[3]-x[2])))
    rel10=float(y4[2]+((y4[3]-y4[2])*(val1-x[2])/(x[3]-x[2])))
    rel11=float(y5[2]+((y5[3]-y5[2])*(val1-x[2])/(x[3]-x[2])))
    rel12=float(y6[2]+((y6[3]-y6[2])*(val1-x[2])/(x[3]-x[2])))
   
elif val1>x[3] and val1<x[4]:
    rel7=float(y1[3]+((y1[4]-y1[3])*(val1-x[3])/(x[4]-x[3])))
    rel8=float(y2[3]+((y2[4]-y2[3])*(val1-x[3])/(x[4]-x[3])))
    rel9=float(y3[3]+((y3[4]-y3[3])*(val1-x[3])/(x[4]-x[3])))
    rel10=float(y4[3]+((y4[4]-y4[3])*(val1-x[3])/(x[4]-x[3])))
    rel11=float(y5[3]+((y5[4]-y5[3])*(val1-x[3])/(x[4]-x[3])))
    rel12=float(y6[3]+((y6[4]-y6[3])*(val1-x[3])/(x[4]-x[3])))
   
elif val1>x[4] and val1<x[5]:
    rel7=float(y1[4]+((y1[5]-y1[4])*(val1-x[4])/(x[5]-x[4])))
    rel8=float(y2[4]+((y2[5]-y2[4])*(val1-x[4])/(x[5]-x[4])))
    rel9=float(y3[4]+((y3[5]-y3[4])*(val1-x[4])/(x[5]-x[4])))
    rel10=float(y4[4]+((y4[5]-y4[4])*(val1-x[4])/(x[5]-x[4])))
    rel11=float(y5[4]+((y5[5]-y5[4])*(val1-x[4])/(x[5]-x[4])))
    rel12=float(y6[4]+((y6[5]-y6[4])*(val1-x[4])/(x[5]-x[4])))
   
elif val1>x[5] and val1<x[6]:
    rel7=float(y1[5]+((y1[6]-y1[5])*(val1-x[5])/(x[6]-x[5])))
    rel8=float(y2[5]+((y2[6]-y2[5])*(val1-x[5])/(x[6]-x[5])))
    rel9=float(y3[5]+((y3[6]-y3[5])*(val1-x[5])/(x[6]-x[5])))
    rel10=float(y4[5]+((y4[6]-y4[5])*(val1-x[5])/(x[6]-x[5])))
    rel11=float(y5[5]+((y5[6]-y5[5])*(val1-x[5])/(x[6]-x[5])))
    rel12=float(y6[5]+((y6[6]-y6[5])*(val1-x[5])/(x[6]-x[5])))
    
elif val1>x[6] and val1<x[7]:
    rel7=float(y1[6]+((y1[7]-y1[6])*(val1-x[6])/(x[7]-x[6])))
    rel8=float(y2[6]+((y2[7]-y2[6])*(val1-x[6])/(x[7]-x[6])))
    rel9=float(y3[6]+((y3[7]-y3[6])*(val1-x[6])/(x[7]-x[6])))
    rel10=float(y4[6]+((y4[7]-y4[6])*(val1-x[6])/(x[7]-x[6])))
    rel11=float(y5[6]+((y5[7]-y5[6])*(val1-x[6])/(x[7]-x[6])))
    rel12=float(y6[6]+((y6[7]-y6[6])*(val1-x[6])/(x[7]-x[6])))
   
else:    
    rel7=float(y1[7]+((y1[8]-y1[7])*(val1-x[7])/(x[8]-x[7])))
    rel8=float(y2[7]+((y2[8]-y2[7])*(val1-x[7])/(x[8]-x[7])))
    rel9=float(y3[7]+((y3[8]-y3[7])*(val1-x[7])/(x[8]-x[7])))
    rel10=float(y4[7]+((y4[8]-y4[7])*(val1-x[7])/(x[8]-x[7])))
    rel11=float(y5[7]+((y5[8]-y5[7])*(val1-x[7])/(x[8]-x[7])))
    rel12=float(y6[7]+((y6[8]-y6[7])*(val1-x[7])/(x[8]-x[7])))
   

L8=float(val2/rel7)
L9=float(rel8*L8)
L7=float(rel9*L8)
L11=float(val2/rel10)
L12=float(rel11*L11)
L10=float(rel12*L11)

print(f"los resultados obtenidos mediante interpolación lineal son:")
print(f"la longitud de los eslabones para optimizacion de rectitud son:")
print(f"La longitud del eslabon L1 es: {L7}")
print(f"La longitud del eslabon L2 es: {L8}")
print(f"La longitud del eslabon L3 es: {L9}")
print(f"la longitud de los eslabones para optimizacion de velocidad son:")
print(f"La longitud del eslabon L1 es: {L10}")
print(f"La longitud del eslabon L2 es: {L11}")
print(f"La longitud del eslabon L3 es: {L12}")