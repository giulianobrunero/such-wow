

def such_wow(initial, final):
	l = [i for i in range(initial, final+1)]
	lp = [('SuchWow' if (n%3==0 and n%5==0) else 'Such' if (n%3==0) else 'Wow' if (n%5==0) else n) for n in l]
	return lp

initial = 1
final = 10
print(such_wow(initial, final))