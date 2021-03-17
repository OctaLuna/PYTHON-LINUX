#TUPLAS
#VARIABLES
tupla = (1, "HOLA MUNDO", True, 3.14159, 73, "E = MC2")
#PROGRESO
print(tupla[3])

#EJEMPLO DE TUPLA
#Una tupla no se puede usar asi, se la considera un int un entero y no una tupla
tupla2 = (1)
print(type(tupla2))
#Pero si le pones una coma al final si se considera tupla, cosas de Python
tupla3 = (3.14159,)
print(type(tupla3))
########################
#Se puede sumar las tuplas???, si se puede
tupla += tupla3
print(tupla)
########################
#Se puede desenpaquetar tuplas???, si se puede pero hayq eu asignarle una variable a cada tupla antes
a, b, c, d, e, f, g = tupla
print(f"a {a}, b {b}, c {c}, d {d}, e {e}, g {f}")