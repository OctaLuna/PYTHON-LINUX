import numpy as np
import matplotlib.pyplot as plt
#IMPORTANTE ANTES DE VER ESTO TIENES QUE VER LA CARPETA FUNCIONES Y ENTENDERAS

N = 1000

def f(x):
    return 3**x

#Esto es para poder manipular las funciones, c es una constante mayor a 0
c = 10

x = np.linspace(-15,15, num=N)

#en esta parte estamos manipulando las funciones;
#-f(x)     refleja la grafica respecto al eje x
#f(-x)     refleja la grafica respecto al eje y
#f(x)      esta es la funcion sin modificar
#-f(-x)    esta funcion refleja el el eje "x" y "y"
y = f(x - c)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')