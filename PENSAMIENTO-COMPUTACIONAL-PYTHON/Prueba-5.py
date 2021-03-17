#ESTAMOS JUNTANDO TODO LO APRENDIDO ANTERIORMENTE PARA USAR LAS FUNCIONES
print("                     RAIZ CUADRADA")
#VARIABLES
num = int(input("Escribe un el numero del cual quieres saber su raiz: "))
#FUNCIONES
def EnumeracionExhaustiva(numero):
    respuesta = 0
    while respuesta **2 < numero:
        #print(respuesta)
        respuesta += 1
    if respuesta **2 == numero:
        print(f"La raiz cuadrada del {numero} es {respuesta}")
    else:
        print(f"{numero} no tiene raiz cuadrada exacta")
def Aproximacion(numero):
    epsilon = 0.01
    #esto es para que en el while vaya subiendo el valor proporcionalmente hasta llegas al resultado
    paso = epsilon**2
    #esto es la variable de la respuesta
    respuesta = 0.0
    while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
        #print(respuesta)
        #Estamos sumando un epsilon al cuadrado a el resultado para llegar al correcto, estamos usando enumeracion exhaustiva
        respuesta += paso
    if abs(respuesta**2 - numero) >= epsilon:
        print(f"No se encontro la raiz cuadrada del {numero}")
    else:
        print(f"La raiz cuadrada de {numero} es la {respuesta}")
def BusquedaBinaria(numero):
    epsilon = 0.01
    #Estamos poniendo el valor menor que puede tener 
    bajo = 0.0
    #max(1.0, objetivo)    lo que esta pasando es que le estamos pidiendo a la variable que nos  regrese el valor mayor entre los 2 valores
    alto = max(1.0, numero)
    #lo que estamos haciendo en esta parte es dividir el resultado en a la mitad, para que? lo hacemos para tantear el terreno para encontrar el numero que escribio 
    respuesta = (alto + bajo) / 2
    #lo que estamos haciendo es buscar el valor, hasta que la variable de respuesta al cuadrado menos objetivo sea mayor a el epsilon seguira en el bucle while
    while abs(respuesta **2 - numero) >= epsilon:
        #Esta parte nunca va a pasar en la primera vuelta de while, por que? por que en la primara vuelta respuesta al cuadrado siempre sera mayo que objetivo Ej: 40,5 ** 2 = 1640.25 < 81, por que en la primera vuelta respuesta tendra el valor de objetivo dividido entre 2
        #En las demas vueltas si puede ser veredicno este dato, normalmente se activa este if unas 2 vueltas despues o 3, en el momento en el que lo alto ya se divide mas veces para encontrar la respuesta
        if respuesta**2 < numero:
            #en esta parte la variable bajo toma el valor de respuesta que es un dividendo del objetivo, al dividirlo tanteamos el terreno para encontrar la respuesta
            bajo = respuesta
        #Esto pasa siempre primero en el bucle que lo que hace es dividir el objetivo en 2, y vamos partiendo a la mitad el objetivo, por que lo partimos por la mitad y la primera parte de las 2 mitades se considera y la otra no? lo que pasa es que la primera parte de las 2 mitades es la que nos importa, por que es lo mas probable o es lo probable mejor dicho que en esa parte se encuentre la raiz, Ej: 9 dividio entre 2 tenemos 2 mitades, 1234 - 6789 el cinco no lo cuento por que quiero trabajar con enteros para que sea mejor la explicacion, 6-7-8-9 no pueden ser ninguno por puera logica, 6 ** 2 es 36, 7 ** 3 es 49 y etc., por eso se usa la primera mitad
        else:
            #En esta parte la variable alto cambia su valor a el del resultado que en este caso es la divicion del objetivo, esto es por lo explicado anteriormente, Ej: 9 dividido entre 2 es 4.5, que en este caso se vuelve en el rango mayor que ahora es 0.0 a 4.5
            alto = respuesta
        #en esta parte estamos subdividiendo para que cada vez alla menos resultados posibles
        respuesta = (alto + bajo) / 2
        #print(f"bajo = {bajo}, alto = {alto}, respuesta = {respuesta}")
    

    print(f"La raiz cuadrada de {numero} es {respuesta}")

#PROGRESO
print("\n\n\n\n Ya falta poco para que sepas la raiz cuadrada que quieres, solo te haremos unas preguntas \n")
pregunta = int(input("De que manera quieres que se resuelva tu raiz:\n 1. Enumeracion Exhaustiva \n 2. Aproximacion \n 3. Busqueda Binaria \n Respuesta: "))
if pregunta == 1:
    EnumeracionExhaustiva(num)
elif pregunta == 2:
    Aproximacion(num)
elif pregunta == 3:
    BusquedaBinaria(num)
else:
    print(f"Algo paso lo que escribiste fue incorrecto {pregunta} vuelve a intentar")