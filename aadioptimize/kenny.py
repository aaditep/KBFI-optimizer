import numpy as np

def kenny(X):
	x=X[0]
	y=X[1]
	F = np.sin(x+y) +(x-y)**2-(1.5*x)+(2.5*y)+1
	return F

#print(kenny([-0.54719,-1.54719]))