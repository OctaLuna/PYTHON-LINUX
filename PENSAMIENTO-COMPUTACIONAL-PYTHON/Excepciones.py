#VARIABLES
usuario = int(input("Escribe un numero para dividir los numeros primos del 2 al 23: "))

#FUNCIONES
def DivideElementosDeListas(lista, divisor):
    #Estamos haciendo programacion defenciba, porque se llama asi???, por que estamos buscando un error posible en el codigo;
    #try es para defendernos del usuario, si cometen un error comun como dividirlo entre 0 saldra error por eso usamos eso, para preparanos 
    try:    
        return [i / divisor for i in lista]
    #Esto es para hacer excepciones en el codigo por lo anteriormente explicado, ZeroDivisionError es un error al dividirlo enter 0; as e: es para referenciar el error
    except ZeroDivisionError as e:
        print(f"Este es el nombre del error: {e}")
        return lista

#PROGRESO
lista = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(DivideElementosDeListas(lista, usuario))