#VARIABLES
nom = str(input("Escribe tu nombre: "))
ape = str(input("Escribe tu apellido: "))
orden = bool(input("En orden quieres tu que escribamos tu nombre primero apellido y despues nombre es True, primero nombre y despues apellido es False: "))
#FUNCIONES
def nombreCompleto(nombre, apellido, inverso = False):
    if inverso == True:
        return f"Tu nombre es {apellido} {nombre}"
    else:
        return f"Tu nombre es {nombre} {apellido}"

#PROGRESO
nombreCompleto(nom, ape, orden)
print(nombreCompleto(nom, ape, orden))