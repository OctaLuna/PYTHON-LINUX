#ESTAMOS PROBANDO LAS EXCEPCIONES
#VARIABLES
#Estamos pidiendo un valor al usuario
usuario = str(input("Escribe el nombre del pais donde vives, con mayuscula la primera letra : "))
#Esta es nuestra lista de paises "Diccionario"
paises = {
    "España": 1,
    "Inglaterra": 2,
    "Francia": 3,
    "Holanda": 4,
    "Estados Unidos": 5,
    "Irlanda": 6,
    "Italia": 7,
    "Roma": 8,
    "Bolivia": 9,
}
#FUNCIONES
#Estamos 
def BusquedaDePaises(paises, pais):
    try:
        return paises[pais]
    except KeyError as e:
        print(f"Este es el nombre del error: {e}")
        return None

#PROGRESO
print(f"El lugar de nuestra lista donde esta tu pais es: {BusquedaDePaises(paises, usuario)}")