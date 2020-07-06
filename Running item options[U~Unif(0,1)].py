import numpy as np 

rand_uni=np.random.uniform(0.0, 1.0, 10) 

rand_exp1=-np.log(1-rand_uni) 

rand_exp2=-np.log(rand_uni) 

print(rand_exp1)

print(np.mean(rand_exp1)) 

print(rand_exp2) 

print(np.mean(rand_exp2)) 
