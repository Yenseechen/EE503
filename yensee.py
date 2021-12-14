from numpy import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"Part a"
expected_time_100 = 100 * 0.25 #hours

"Part b"

exp_100 = np.random.exponential(0.25, 100)


"Part c"

t1 = np.sum(exp_100)


"Part d"
d= 1000

n = list(range(1, d))
mean_exp=[]

for i in n:
    mean_e = 0
    for j in range(i):
        mean_e = mean_e + np.sum(np.random.exponential(0.25, 100))
    
    mean_e = mean_e / i
    mean_exp.append(mean_e)
    

plt.plot(n,mean_exp)
plt.show()

"Part e"


for i in range(d-50):
    flag = 0
    for j in range(50):
        if mean_exp[i+j]<expected_time_100*0.98 or mean_exp[i+j]>expected_time_100*1.02 :
            flag = 1
    
    if flag == 0:
        print("Minimum values of n: ",end =" ")    
        print(i)
        break
        
        
        