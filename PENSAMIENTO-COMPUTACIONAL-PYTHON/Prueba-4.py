#busqueda-binaria prueba
#VARIABLES
usuario = int(input("Escribe un numero: "))
epsilon = 0.01
minimo = 0.0
maximo = max(epsilon, usuario)
res = (minimo + maximo) / 2
#PROGRESO
while abs(res ** 2 - usuario) >= epsilon:
    if res**2 < usuario:
        minimo = res
    else:
        maximo = res
    res = (minimo + maximo) / 2
print(f"La raiz de {usuario} es {res}")
