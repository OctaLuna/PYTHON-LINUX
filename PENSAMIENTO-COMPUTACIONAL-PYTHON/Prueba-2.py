#VARIABLES
nom = str(input("Escribe tu nombre: "))
edad = int(input("Escribe tu edad: "))
nom2 = str(input("Escribe el nombre de otra persona: "))
edad2 = int(input("Escribe la edad del la otra persona que escribiste: "))
estado = None
#FUNCINES
def persona(nombre, edad, nombre2, hola):
    print(f"Tu nombre es {nombre}, tu edad es {edad}, si lo comparamos con la edad de {nombre2}, tu eres {hola}") 
#PROGRESO

if edad > edad2:
    estado = "mayor"
    persona(nom, edad, nom2, estado)
elif edad < edad2:
    estado = "menor"
    persona(nom, edad, nom2, estado)
elif edad == edad2:
    estado = "de su misma edad"
    persona(nom, edad, nom2, estado)