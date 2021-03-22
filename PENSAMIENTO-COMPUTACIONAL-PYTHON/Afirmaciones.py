#VARIABLES
ListaDePalabras = {"HOLA", "COMO", "ADIOS"}
#FUNCIONES
def PrimeraLetra(ListaDePalabras):
    PrimerasLetras = []
    for palabra in ListaDePalabras:
        #En esta parte nos estamos defendiendo del usuario, estamo poniendo probabilidades que puede pasar cuando el usuario escriba el input, Ej: si el tipo de palabra no es str envia el mensaje de "Lo que escrobiste no es un str"; 
        assert type(palabra) == str, f"Lo que escriste no es un str, {palabra}"
        assert len(palabra) > 0, "No escribiste nada..."
    PrimerasLetras.append(palabra[0])
    return PrimerasLetras

#PROGRESO
print(f"Las primeras letras de la lista son: {PrimeraLetra(ListaDePalabras)}")
    