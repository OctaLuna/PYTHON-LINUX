#HACI SE CREAN  QUE SI SON MUTABLES A DIFERENCIA DE LAS TUPLAS
myList = [3.141519, 3, "HOLA MUNDO DE NUEVO JEJEJ"]
print(myList[1])
print("\n")
###########
# es para decirle que vaya del numero 1 hasta el final, recuerdad la estructura con la misma que trabaja las tuplas, [INICIO: FINAL: PASOS]
print(myList[1:])
print("\n")
###########
#Le podemos aumentar valores a las list
myList.append("HOLA DE NUEVO")
print(myList)
print("\n")
###########
#Podemos cambiar de valores las listas
myList[2] = 73
print(myList)
print("\n")
###########
#Borra el ultimo valor de las listas
myList.pop()
myList.pop()
print(myList)
print("\n")
###########
#Esto es para que imprima todos los elementos de la lista
for elements in myList:
    print(elements)
print("\n")
###########
print("\n \n \n \n \n")
#ERRORES POTENCIALES EN LISTAS, AL CAMBIAR Y AUMENTAR VALORES
#Usamos otra lista
a = [1, 2, 3, "a", "b", "c"]
# Asignamos a b con el mismo valor que a
b = a
print(f"Estamos imprimiendo a: {a}")
print(f"Estamos imprimiendo a: {b}")
print(f"Estamos buscando el espacio de a en la memoria: {id(a)}")
print(f"Estamos buscando el espacio de a en la memoria: {id(b)}")
print("Nos dimos cuenta de que a y b llaman a el mismo espacio en memoria")
#Creamos otra lista con los valores de a y b
c = [a, b]
print(f"Estamos imprimiendo c: {c}")
#Estamos aumentando una variable a la lista de a
a.append("d")
print(f"Estamos imprimiendo c para ver como cambio el valor de a : {c}")
print("Ahora vemos que cambio el el valor de las lista de a y b, esto paso por que las 2 variables llaman a el mismo lugar en memoria y por logica tiene el mismo valor")
