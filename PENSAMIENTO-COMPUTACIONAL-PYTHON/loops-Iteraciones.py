#VARIABLES
contadorExterno = 0
contadorInterno = 0
#PROGRESO
while contadorExterno < 10:
    while contadorInterno < 10:
        print(contadorExterno, contadorInterno)
        contadorInterno += 1
    print()
    contadorExterno += 1
    contadorInterno = 0
    