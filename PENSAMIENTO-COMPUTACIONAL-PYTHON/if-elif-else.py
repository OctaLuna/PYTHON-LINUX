#VARIABLES
num = int(input("Escoge un entero: "))
num2 = int(input("Escoge otro entero: "))

if num > num2:
    print("El primer numero es mayor que el segundo")
elif num < num2:
    print("El segundo numero es mayor que el primero")
elif num == num2:
    print("El primer numero es igual al segundo numero")
else:
    print("Algo salio mal vuelve a intentar")