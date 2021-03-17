#VARIABLES
#Esto es una funcion en exprecion, lambda <variables>: <exprecion>
sumar = lambda a, b: a + b
multiplicar = lambda a, b: a * b
resta = lambda a, b: a - b
#PROGRESO
num = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))
pregunta = int(input("Ahora que escribiste los numeros, dime como los queres operar\n 1. suma \n 2. multiplicacion \n 3.resta\n Respuesta: "))

if pregunta == 1:
    print(sumar(num, num2))
elif pregunta == 2:
    print(multiplicar(num, num2))
elif pregunta == 3:
    print(resta(num, num2))
else:
    print("UFFFF, no es valido vualve a escribirlo...")