from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

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
 
 
 
#lo primero que hacermos es un mapa de niveles que vamos a estar graficando
#lo que estamos haciendo es que estamos diciendo que el inicio seria el minimo de Z y el final sera el maximo de Z 
level_map = np.linspace(np.min(Z), np.max(Z), res)
 
#Ahora generamos un contorno a la figura
plt.contourf(X, Y, Z, levels=level_map, cmap=cm.cool)
#Le estamos agregando una barra de colores
plt.colorbar()
#le estamos agregando un titulo
plt.title("Decenso de gradiente")
#
#
#
#
#
