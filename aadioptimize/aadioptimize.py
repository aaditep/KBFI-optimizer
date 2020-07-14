from sphere import spherex
import numpy as np
# User inputid are: fitness function, lowerbound(lb),upperbound(ub), populatonsize(N_p)
#number of iterations(T), scaling factor F, crossover probability(P_c)


#problem settings
lb = np.array([0,0,0,0,0])
ub = np.array([10,10,10,10,10])


#Paramaters for Differential Evlution

N_p = 5 #Number of population
T = 100 #number of iterations
P_c = 0.8 #crossover probability
F = 0.85 #scaling factor

#Initializing DE