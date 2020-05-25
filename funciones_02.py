def suma(valor_uno, valor_dos, valor_tres):
	return valor_uno + valor_dos + valor_tres

def division(valor_uno, valor_dos):
	return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos = 10):
	return valor_uno * valor_dos

def multiples_valores():
	return "string", 1, True, 26.6   

def  mostrar_resultado ( funcion ):
	print(funcion(6,8))

mi_variable = multiplicacion
mostrar_resultado( mi_variable )
