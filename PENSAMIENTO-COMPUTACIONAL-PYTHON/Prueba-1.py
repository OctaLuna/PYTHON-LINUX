#VARIABLES
#Este es el nombre que estamos pidiendo
nom = str(input("Escribe tu nombre: "))
#Este es el apellido que estamos pidiendo
ape = str(input("Escribe tus apellidos: "))
#Estos son los caracteres que tiene el nombre que escribieron
CaracteresNom = len(nom)
#Estos son los caracteres que tiene el apellido que escribieron
CaracteresApe = len(ape)
#Estamos sumando los caracteres del apellido y nombre
CaracteresNomCompleto = CaracteresNom + CaracteresApe
#PROGRESO
#Estamos juntando todo
res = f"En hora buena, tu nombre y apellido es {nom} {ape} y tu nombre tiene {CaracteresNomCompleto - 1} caracteres"
#Lo estamos imprimiendo
