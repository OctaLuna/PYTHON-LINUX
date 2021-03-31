import numpy as np
import matplotlib.pyplot as plt

#Esta es la primera funcion
def g(x):
  return 2**x
#Esta es la segunda funcion
def f(x):
  return np.cos(x)

x = np.linspace(-1,10, num=1000)

#En esta parte estamos juntando las funciones
#f_o_g f es la segunda funcion, ° es el operador de anillo y g es la primera funcion
f_o_g = f(g(x))

fig, ax = plt.subplots()
ax.plot(x,f_o_g)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')