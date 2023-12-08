
# Modulo y libreria

from Funcion import *
import math

# Mostrar funciones de math

print("Info:", help(math))
print("Ceil:", math.ceil(8.0))
print("Floor", math.floor(8.3))

# Funciones

def Escribir(url, texto):
	Abrir(url, "w", texto)

def Leer(url):
	Abrir(url, "r")

def Agregar(url, texto):
	Abrir(url, "a", texto)
	Abrir(url, "a", "\n")

def Borrar(url, palabra):

	with open(url, "r", encoding = "utf-8") as archivo:
		texto = archivo.readlines()

	with open(url, "w", encoding = "utf-8") as archivo:
		for line in texto:
			texto = line.replace(palabra, "")
			texto = archivo.write(texto)