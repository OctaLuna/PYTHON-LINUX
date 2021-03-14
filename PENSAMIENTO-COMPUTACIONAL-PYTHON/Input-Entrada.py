#VARIABLES
#Estamos pidiendo un nombre
nombre = str(input("Escribe tu nombre: "))

#estamos pidiendo numeros para poderlos sumar
num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))
#Esto es la suma que estamos haciendo
suma = num1 + num2
#PROGRESO
#Este es el nombre que pusieron
print(nombre)
resultado = "Tu nombre es Elon Musk, jeje no ahora si tu nombre es : " + nombre
print(resultado)

###########
#Estamos imprimiento la suma que hicimos
print(f"Suma  {num1} + {num2} = {suma}")
