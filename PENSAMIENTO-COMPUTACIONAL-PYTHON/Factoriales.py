#VARIABLES
usuario = int(input("Escribe un numero y sabras cual es su factorial: "))
#FUNCIONES
def factorial(n):
    print(n)
    #Esto es para poder sacar el factorial de un numero, nuestro primer valor es n que hace como n! que es n factorial, pero n es una variable que le estamos asignado
    
    #Lo que estamos haciendo aqui es que si la variable n es igual a 1 pasa esto, esto se hace por que con la formula de n! = n*(n - 1)! el 1 no sale, pero con la formula de extencion si sale
    if n == 1:
        return 1
    #esto es la formula de n! = n*(n - 1)! para resolver factoriales, y si estamos usando una la funcion dentro de la funcion y si se puede, ahora la pregunta por que funciona??? funcion por que estamos haciendo un bucle en la funcion si notaron cada vez que llama a factorial se resta 1 t por eso el if n ==1 para que acabe hay, se resta haci y se multiplica con cada resta que hace, 4 * 3 * 2 * 1
    return n * factorial(n - 1)
#PROGRESO

print(factorial(usuario))