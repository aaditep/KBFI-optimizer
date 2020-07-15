import numpy as np
def beale(X):
	x = X[0]
	y = X[1]
	F=(1.5 -x + x*y)**2+(2.25-x+x*(y**2))**2+(2.625-x+x*(y**3))**2
	return F

#l=[3.,0.5]
#print(beale(l))