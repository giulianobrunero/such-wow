import sys

def such_wow(initial, final):
	l = [i for i in range(initial, final+1)]
	lp = [('SuchWow' if (n%3==0 and n%5==0) else 'Such' if (n%3==0) else 'Wow' if (n%5==0) else n) for n in l]
	return lp

try:
	initial = int(sys.argv[1])
	final= int(sys.argv[2])
	print(such_wow(initial, final)) if initial <= final else print('El valor inicial debe ser menor o igual que el valor final')
except:
	print('Solo se permiten dos valores enteros positivos o negativos, separados por espacios. El primer valor debe ser menor o igual al segundo valor.')
