#Estamos haciendo que el usuario escoja un numero entero para que nosotros podamos comveritirlo en rai<
objetivo = int(input("Escoje un numero: "))
#este numero es a eleccion para que el programa procese los datos con mas veracidad
epsilon = 0.01
#esto es para que en el while vaya subiendo el valor proporcionalmente hasta llegas al resultado
paso = epsilon**2
#esto es la variable de la respuesta
respuesta = 0.0

#prueba = respuesta**2 - objetivo
#Esto es par apoder sacar el aproximado de la raiz cuadra 
#abs es para sacar un valor absoluto, que siempre sea positivo
#abs(respuesta**2 - objetivo) esto es para comprovar que no nos pasamos del resultado
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    #Estamos sumando un epsilon al cuadrado a el resultado para llegar al correcto, estamos usando enumeracion exhaustiva
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontro la raiz cuadrada del {objetivo}")
else:
    print(f"La raiz cuadrada de {objetivo} es la {respuesta}")