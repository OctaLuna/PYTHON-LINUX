#Lo que hicimos primero esque es crear una lista con rangos 
MyList = list(range(100))
print(MyList)
# en esta parte lo multiplicamos por 2 el valor de MyList
double = [i * 2 for i in MyList]
print(double)
#Esto es para poner condicionales
pares = [i for i in MyList if i % 2 == 0]
print(pares)