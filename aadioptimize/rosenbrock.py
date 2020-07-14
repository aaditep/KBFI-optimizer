def rosenbrock(X):
	x = X[0]
	y = X[1]
	f = (1-x)**2 + 100*(y-x**2)**2
	return f


l = [1,1]
print(rosenbrock(l))