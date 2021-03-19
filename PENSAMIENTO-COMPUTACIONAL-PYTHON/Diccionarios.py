#Esto es un diccionario, la diferencia que tiene con las listas es que las listas tienen un indice numero Ej: 0, 1, 2; Pero los diccionarios no se llamando con un nombre o llave
myDict = {
    "Marco" : 16,
    "Octavio" : 25,
    "Orlando" : 55,
}
print(myDict)
print("Estamos imprimiendo el valor de Marco en nuestro diccionario que es:")
print(myDict["Marco"])
############
#Mutar un valor o cambiando el valor que tenia la llave de Octavio
myDict["Octavio"] = 80 
print(myDict)
############
#Estamos aumentando el valor de Juan a nuestro diccionario
myDict["Juan"] = 2
print(f" Se adiciono el una nueva variable para el diccionario que es \n{myDict}")
############
#Esto es para borrar un valor de nuestro diccionario
del myDict["Orlando"]
print(f"Ufff borramos a Orlando de el diccionario Un tipo de lista, ahora mira como quedo: \n {myDict}")
############
#Esto es para imprimir solo las llaves de cada variable del diccionario
for llaves in myDict.keys():
    print(llaves)
#esto es para imprimir el valor de las variables del diccionario
for valor in myDict.values():
    print(valor)
