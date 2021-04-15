from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
  return x**2 + y**2

#Esta es la resolucion de nuestra grafica bueno de los vectores "x" y "y"
res = 1000

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
level_map = np.linspace(np.min(Z), np.max(Z),res)
 
#Ahora generamos un contorno a la figura
plt.contourf(X, Y, Z, levels=level_map,cmap=cm.cool)
#Le estamos agregando una barra de colores
plt.colorbar()  
#le estamos agregando un titulo
plt.title("Decenso de gradiente")
###
def derivate(cp,p):
  #en esta parte estamos usando la funcion derivada
  #la formula es      lim           f(x) -f(x)
  #                                     h
  #                   h --> 0       
  return  (f(cp[0],cp[1]) - f(p[0],p[1])) / h


#Le estamos asignando un punto aleatorio para hacer el decenso de gradientes
#pn.random.rand nos regresa un numero aleatorio entre 0 y 1
# (2)como es una funcion vidimencional vamos a usar 2 valores
# * 8 - 4 esto se hace por los contornos que tiene los parametros de la tapla que son (-4y a 4y) y (-4x a 4x)
#le restamos un 4 para que si el rand(0) es 0 el valor minimo sea 4
#Y tambien sirve al revez si el rand(0) es 1 el valor se multiplica por por 8 y se resta por 4, que eso nos da el valor mayor
p = np.random.rand(2) * 8 - 4
#Esto es para graficar este punto
#p[0], p[1] esto 2 es para poner los limites que de un numero de 0 a 1
#"o" es para que grafique un punto
#c="k" es para que sea negro
plt.plot(p[0],p[1],'o', c='k')


#rl es lo mismo que h
lr = 0.01
#esto es para tener una valor muy pequeño para poder hacer el incremento
h = 0.01


#Esto es para que suceda el desenso de gradiente, para el punto vaya a el valor minino de la figura
def gradient(p):
  #Este es un vector que va a estar lledado con ceros
  grad = np.zeros(2)
  #estamos iterando 
  #idx esta variable significa indice de x
  #val es valor
  #enmerate es para que se enumere hasta el valor de p
  # lo que hace esta funcion es que la derivada la va a calcular dependiente al componente idx 
  for idx, val in enumerate(p):
    #Estamos sacando una copia del punto
    cp = np.copy(p)
    #esto es para que tenga el incremento de la funcion para que se acerque mas a el valor minimo
    cp[idx] = cp[idx] + h;
    #AHORA DEVEMOS CALCULAR LA DERIVADA PARCIAL
    #dp es derivada parcial
    #derivate es para calcular la derivada es una funcion que nosotros creamos y esta funcion va requerir nuestra copia y nuestro punto original
    dp = derivate(cp,p) 
    # y ahora solo nos falta definir el vector que definimos lleno de 0
    grad[idx] = dp

    #ahora retornamos este gradiente
  return grad

#AHORA HAREMOS EL PROCESO ITERATIVO QUE ES ESO DE QUE LOS PUNTOS SE VAN ACERCANDO CADA VEZ MAS A EL VALOR MINIMO DE LA FUNCION
#Ahora lo que sigue es definir el proceso iterativo de nuestro algoritmo
#esto va de tener nuestro punto y irlo actualizando para que se hacerque cada vez mas
for i in range(10000):
  #p es nuestro punto
  # lo que estamos haciendo es que p = p "el mismo punto " - lr "es una variable creada anteriormente" * gradient(p) "que es la funcion que creamos para sacar el gradiente"
  p = p - lr*gradient(p)
  #Esto es para plotear osea que alla 10 puntos para que se hacerque a el valor minimo
  #Esto es va a pasar que al hacer i % 10 el residuo sea igual a 0
  if(i % 10 == 0):
    #Esto es para graficar el punto pero estavez en color rojo
    plt.plot(p[0],p[1],'o', c='r')

#Este es punto blanco, es el punto final
plt.plot(p[0],p[1],'o', c='w')
