'''
##### Script such_wow #####

# Recibe: Desde la linea de comandos, separados por espacios, dos valores enteros como parametros.
	* Los dos valores pueden ser enteros positivos o enteros negativos.
	* El primer valor debe ser menor o igual al segundo valor.
# Retorna: La impresion de una lista con ciertos valores remplazados por palabras clave:
	* Si el numero es multiplo de 3 y de 5: Se remplaza por 'SuchWow'
	* Si el numero es multiplo de 3: Se remplaza por 'Such'
	* Si el numero es multiplo de 5: Se remplaza por 'Wow'
'''

import sys

def such_wow(initial, final):
	# Creacion de la lista.
	l = [i for i in range(initial, final+1)]
	# Remplazo los multiplos de la lista por las palabras clave y obtengo la lista parceada.
	lp = [('SuchWow' if (n%3==0 and n%5==0) else 'Such' if (n%3==0) else 'Wow' if (n%5==0) else n) for n in l]
	# Retorno la lista parceada.
	return lp

try:
	initial = int(sys.argv[1])
	final= int(sys.argv[2])
	print(such_wow(initial, final)) if initial <= final else print('El valor inicial debe ser menor o igual que el valor final')
except:
	print('Solo se permiten dos valores enteros positivos o negativos, separados por espacios. El primer valor debe ser menor o igual al segundo valor.')
