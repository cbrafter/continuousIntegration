def Fibonacci(n):
	if n < 0:
		raise ValueError('n<0 invalid')
	elif type(n) != int:
		raise ValueError('n not int')
	else:
		a,b = 1,1
		for i in range(n-1):
			a,b = b,a+b
		return a

