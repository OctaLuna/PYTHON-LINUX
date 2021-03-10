#VARIABLES
#Monedas
Dolar = 0.14
Euro = 0.12
#
MonedaCambiada = "moneda"

monedaCambio = int(input("Escribe el valor de la moneda Bs que quieres cambiar: "))
TipoDeMoneda = bool(input("Escribe True si quieres cambiar el valor de la moneda a Dolar y escribe False si quieres cambiar el valor de la moneda por Euro: "))
if TipoDeMoneda == True:
	resultado = monedaCambio * Dolar
	MonedaCambiada = "Dolar "
	print("Cambio " + str(monedaCambio) + "Bs" + ", lo cambiaste a " + MonedaCambiada + str(resultado))
elif TipoDeMoneda == False:
	resultado = monedaCambio * Euro
	MonedaCambiada = "Euro "
	print("Cambio " + str(monedaCambio) + "Bs" + ", lo cambiaste a " + MonedaCambiada + str(resultado))
else:
	print("Pusiste un valor no apropiado, intenta de nuevo")
