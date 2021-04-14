from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

#Estamos definiendo nuestra funcion con mas de una variable independiente
def z(x,y):
  return np.sin(x) + 2*np.cos(y)

#Esta es la resolucion de nuestros vectores
res = 100

#En esta parte estamos marcando nuestros vectores
x = np.linspace(-4, 4, num=res)
y = np.linspace(-4, 4, num=res)

#Esta es la funcion que nos permite juntar la combinacion de puntos de "x" y "y"
x, y = np.meshgrid(x,y)

#Estamos asignando la funcion que hicimos a una variable
z = z(x,y)

#subplot_kw={"projection":"3d"} en esta parte le estamos diciendo que vamos a graficar en una superficie en 3D
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

#esto es para que porfin pueda graficar
# cmap=cm.cool esto es para que le podamos agregar colores
surf = ax.plot_surface(x,y,z, cmap=cm.cool)

#Y finalmente esto es para que tenga una barra de colores alado de la grafica
fig.colorbar(surf)
