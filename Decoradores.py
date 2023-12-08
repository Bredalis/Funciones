
def Decorador(espacio):
	def Funcion_Interna():

		print("Inicio")
		espacio()
		print("Final")

	return Funcion_Interna

@Decorador
def Suma():
	print(1 + 2)

Suma()