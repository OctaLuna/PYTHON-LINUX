import numpy as np
import matplotlib.pyplot as plt
#IMPORTANTE ANTES DE VER ESTO TIENES QUE VER LA CARPETA FUNCIONES Y ENTENDERAS

N = 1000

def f(x):
    return x**2

#Esto es para poder manipular las funciones, c es una constante mayor a 0
c = 10

x = np.linspace(-15,15, num=N)

#en esta parte estamos manipulando las funciones;
#f(x) * c       Alargar la grafica verticalmente en un factor de c
#f(x) * (1/c)   Comprimir la grafica verticalmente en un factor de c
#f(x * c)       Comprimir la grafica horizontalmente en un factor de c
#f(x * (1/c))   Alargar la grafica horizontalmente en un factor de c
y = f(x * c)


fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
