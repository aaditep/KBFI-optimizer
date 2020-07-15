import numpy as np
def rastrig(x):
	n=1
	A= 10
	f=np.sum((A*n)+(x**2-10* np.cos(2*np.pi*x)))
	return f

print(rastrig(0))