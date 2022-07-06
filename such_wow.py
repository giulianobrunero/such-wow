import sys

def such_wow(initial, final):
	l = [i for i in range(initial, final+1)]
	lp = [('SuchWow' if (n%3==0 and n%5==0) else 'Such' if (n%3==0) else 'Wow' if (n%5==0) else n) for n in l]
	return lp

initial = int(sys.argv[1])
final= int(sys.argv[2])

print(such_wow(initial, final))