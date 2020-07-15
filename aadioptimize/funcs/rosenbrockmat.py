import numpy as np
def rosenbrock(X):
	d=len(X) #elementide pikkus
	f =np.zeros((d-1,1))
	for i in np.arange(d-1):
		f[i]= 100*((X[i])**2- X[i+1])**2+(1-X[i])**2
	F=sum(f)
	return F