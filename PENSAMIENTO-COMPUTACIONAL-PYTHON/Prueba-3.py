#Estamos haciendo que el usuario escoja un numero entero para que nosotros podamos comveritirlo en rai<
objetivo = int(input("Escoje un numero: "))
#este numero es 
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0

#prueba = respuesta**2 - objetivo
#Es para que te regrese el valor absoluto abs
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta)
    respuesta += paso
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontro la raiz cuadrada del {objetivo}")
else:
    print(f"La raiz cuadrada de {objetivo} es la {respuesta}")