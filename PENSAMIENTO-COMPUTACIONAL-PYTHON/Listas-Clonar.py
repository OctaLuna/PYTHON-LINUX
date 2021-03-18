#
a = [1, 2, 3, 4, 5]
print(f"Este es el id de a: {id(a)}")
b = a
print(f"Estamos sacando el id de b para ver si es igual a el de la a: {id(b)}")
#list es para clonar una lista
c = list(a)
print(f"Ahora estamos sacando el id de c para ver si es igual al de la a{id(c)}")
print(f"ahora que paso por que c no es igual a bueno su id... \n El id de a es: {id(a)}\n El id de b es: {id(b)}\nEl id de c es: {id(c)}\n Esto pasa por que enves de asigna el valor de a en c lo clonamos")