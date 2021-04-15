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




#Estamos creando otra figura y otro eje
fig2,ax2 = plt.subplots()
#estamos creando una mapa de niveles
#min(z) estamos buscando nuestro valor minimo de nuestra funcion
#max(z) estamos buscando nuestro valor mayor de nuestra funcion
#por ultimo estamos dandole la resolucion 
level_map = np.linspace(np.min(z), np.max(z), num=res) 

# Estamos graficando
#ax2 estamos usando el eje 2 que creamos
#contour(x, y, z, levels=level_map,cmap=cm.cool) esto es para que lo grafique deacuerdo a los niveles que creamos y los mapas de colores creados anteriormente 
cp = ax2.contour(x, y, z, levels=level_map,cmap=cm.cool)

#esto es para que en la figura 2 se agregen la bara de colores
fig2.colorbar(cp)