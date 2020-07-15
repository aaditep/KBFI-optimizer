import numpy.matlib as mat
#from sphere import spherex
import numpy as np
#from rosenbrockmat import rosenbrock
#from shaffer import shaffer
from kenny import kenny
from rosenbrock import rosenbrock
from Beale import beale
# User inputid are: fitness function, lowerbound(lb),upperbound(ub), populatonsize(N_p)
#number of iterations(T), scaling factor F, crossover probability(P_c)


#problem settings
lb = np.full(5,-4.5) #generates column of n bounds(nr. of rows, bound)
ub = np.full(5,4.5)


#Paramaters for Differential Evlution

N_p = 5 #Number of population
T = 1000 #number of iterations
P_c = 0.5 #crossover probability
F = 0.85 #scaling factor

#Initializing DE
f = np.zeros((N_p,1)) #empty vector for fitness function

fu = np.zeros((N_p,1))#newly created trial vector

D = len(lb) # Determining amount of decision variables

U = np.zeros((N_p,D)) #Matrix for storing trial solutions 

#Initial random population !!!!!MIND THE "LEN", I DONT KNOW if that works"
P = mat.repmat(lb,N_p,1)+mat.repmat((ub-lb),N_p,1)*np.random.rand(len(ub-lb),N_p)

#initial fitness function values to f as a vector
for p in np.arange(N_p):
    f[p]=kenny(P[p,])
print(f)



#iteration loop
for t in np.arange(T):

    for i in np.arange(N_p):
        
        
        print(t)
        #MUTATION
        #candidates are assigned without the i-th element
        candidates= np.delete(np.arange(N_p), np.where(np.arange(N_p)==i))
        #3 target vectors are picked out randomly for the donorvector generator
        cand_rand=np.random.choice(candidates,3,replace= False)
        X1=P[cand_rand[0],]
        X2=P[cand_rand[1],]
        X3=P[cand_rand[2],]
        #Donorvctor generator
        V= X1 + F*(X2-X3)
        
        
        #Crossover
        delta = np.random.randint(0,D-1) 
        for j in np.arange(D):
            if np.random.uniform(0,1) <= P_c or delta == j:
                U[i,j] = V[j]
            else:
                U[i,j]=P[i,j]
                
        
       ##Bounding and Greedy Selection

    for j in np.arange(N_p):
        U[j]=np.minimum(U[j], ub)
        U[j]=np.maximum(U[j], lb)
    
        fu[j]=kenny(U[j])
    
        if fu[j] < f[j]:
            P[j]= U[j]
            f[j]=fu[j]
 



print(f'Final iteration results for P:\n{ P}')
print(f'Fitness function values \n{f}')
best_of_f= min(f)
print(f'Best fitness function value{best_of_f}')
print(f'Best fitness value location/row {f.argmin()}')
print(f'Best solution {P[f.argmin()]}')