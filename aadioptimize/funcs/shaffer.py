import numpy as np
def shaffer(X):
	x1 = X[0]
	x2 = X[1]

	fact1 = (np.sin(x1**2-x2**2))**2-0.5
	fact2 = (1+0.001*(x1**2 + x2**2))**2
	F = 0.5 + fact1/fact2
	return F


#print(shaffer([0,0]))