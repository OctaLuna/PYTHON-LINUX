from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

#Primero asignamos nustra figura y eje
#subplot_kw={"projection": "3d"} le estamos diciendo que nos grafique una mapa de 3 dimenciones
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

def f(x,y):
  return x**2 + y**2

#Esta es la resolucion de nuestra grafica bueno de los vectores "x" y "y"
res = 100

#Esto es para graficar nuestro vector x
x = np.linspace(-4, 4, res)

#Esto es para graficar nuestro vector y
y = np.linspace(-4,4, res)

#Esto es para generar nuestros vectores "x" y "y" pero ya con nuestra serie de puntos
X, Y = np.meshgrid(x, y)

#Estamos definiendo nuestro vector Z con los puntos de la funcion f
Z = f(X, Y)

#Por fin graficamos 
#Esto es parar graficar nuestra superficie
#cmap=cm.cool esto es para el color
surf = ax.plot_surface(X, Y, Z, cmap=cm.cool)

fig.colorbar(surf)