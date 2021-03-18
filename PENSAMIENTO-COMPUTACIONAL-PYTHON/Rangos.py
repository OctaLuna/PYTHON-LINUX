#RANGOS range(inicio, final, pasos)
#Estamos hablando haciendo rangos, el inicio es 1 , el final es 5, y no hay pasos que es una forma de saltar ente cantidades Ej:range(1, 10, 2) 1, 3, 5, 7, 9..
myRange = range(1, 4, 2)
type(myRange)
#Estamos haciendo un for, donde myRange lo esta tomando como el valor final que es 5
for i in myRange:
    print(i)
print("\n\n\n\n")
#########
myRange = range(0, 20, 3)
myOtherRange = range(0, 15, 2)
#myRange == myOtherRange esto saldra True
for i in myRange:
    print(i)
#####Buscar todos los numeros pares
for i in range(0, 101 , 2):
    print(f"numero {i}")