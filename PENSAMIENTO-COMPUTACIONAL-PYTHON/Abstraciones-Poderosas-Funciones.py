#PROBLEMA NO ENTENDIDO
#FUNCIONES
def MultiplicarPorDos(n):
    return n * 2
def SumaDos(n):
    return n + 2
def AplicacionOperaciones(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

nums = [1, 2, 3]
print(AplicacionOperaciones(MultiplicarPorDos, nums))
print(AplicacionOperaciones(SumaDos, nums))