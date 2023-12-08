
print("Agrupador de edades menores")

lista_edades = []
pregunta = ""

"""
Bucle que le pide 
al usuario que ingrese 
las edades que quiera
"""

while pregunta != "No":

	try:
		elementos = int(input("Introduce edad: "))
		lista_edades.append(elementos)

	except ValueError:
		print("Solo numeros")

	finally:
		pregunta = input("¿Quieres seguir ingresando edades? (Si/No): ").capitalize()

def Edades_Menores(edades):
	return edades <= 18

# Filtrando las edades menores

filtro = list(filter(Edades_Menores, lista_edades))

print("Edades Menores:", filtro)