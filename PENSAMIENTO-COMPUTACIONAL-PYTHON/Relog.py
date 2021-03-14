#IMPORTACION
import time

#VARIABLES
hora = 0
minuto = 0
segundo = 0
#PROGRESO
print("Hora Minuto Segundo")
while hora < 24:
    while minuto < 60:
        while segundo < 60:
            print(hora, minuto, segundo)
            time.sleep(1)
            segundo += 1
        minuto += 1
        segundo = 0
    hora += 1
    minuto = 0     
print("PASO UN DIA COMPLETO JEJE")