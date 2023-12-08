
def Decorador(espacio):
	def Funcion_Interna(base, exponente):

		print("Inicio")
		espacio(base, exponente)
		print("Final")

	return Funcion_Interna

@Decorador
def Potencia(base, exponente):
	print(pow(base, exponente))

Potencia(base = 1, exponente = 8)