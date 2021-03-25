import matplotlib.pyplot as plt
import numpy as np

#Esta es la funcion algebraica polinomial
def f(x):
  #Estamos regresando la funcion polinomica
  return x**3

#esto es cuantos puntos tendra nuestro vector -Funcion-Polinomica
n = 100
#esta es la variable independiente 
#np.lispace es un vector que nos genera una serie de puntos en un rango
#(-1, 5,) esto es para ver cual sera el punnto de partida y de llegada, -1 es el punto de partida y 5 es donde termina el vector
#(num=res) estos son cuantos puntos tiene nuestro vector, num es el parametro que lo define
x = np.linspace(-2,  2, num=n)
#Estamos pasando los valores a nuestro funcion
y = f(x)
#Estamos graficando nuestra funcion lineal, matplotlib estamos usando esta libreria
#fig es para optener la figura
#ax es para optener los eje de la grafica que estamos haciendo
#plt es la funcion matplotlib, subplots() es para que se pueda graficar
fig, ax = plt.subplots()
#En esta parte porfin estamos graficando
#ax.plot es para graficar
#(x, y) la grafica nos pide el dominio de la funcion que es el "x", y nos pide la funcion que es la "y"
ax.plot(x, y)
#Esto es para cuadricular el plano carteciano
ax.grid()
#Esto es para poner lineas al plano, en este claso estamos poniendo una linea en horizontal
#ax es para graficar
#axhline es para graficar la linea horizontal que es la linea de la "X" en un plano carteciano
#y = 0 es para que la linea se pongo en el eje de y = 0 por que en ese lugar se encuanta el eje de las x
#color es para ponerle un color a la linea, r es rojo
ax.axhline(y = 0, color="r")
#Esto es para poner lineas al plano, en este claso estamos poniendo una linea en vertical
#ax es para graficar
#axvline es para graficar la linea vertical que es la linea de la "Y" en un plano carteciano
#x = 0 es para que la linea se pongo en el eje de x = 0 por que en ese lugar se encuanta el eje de las y
#color es para ponerle un color a la linea, r es rojo
ax.axvline(x = 0, color="r")