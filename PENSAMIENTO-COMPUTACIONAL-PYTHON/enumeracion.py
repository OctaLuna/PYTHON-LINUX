#VARIABLES
objetivo = int(input("Escoge un numero entero: "))
respuesta = 0

#PROGRESO
while respuesta **2 < objetivo:
    #print(respuesta)
    respuesta += 1
if respuesta **2 == objetivo:
    print(f"La raiz cuadrada del {objetivo} es {respuesta}")
else:
    print(f"{objetivo} no tiene raiz cuadrada exacta")