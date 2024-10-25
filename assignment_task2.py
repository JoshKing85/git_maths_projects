import numpy as np
import math
from assignment_task1 import mean_of_z
#print(mean_of_z)

a = 13
u = (1 + 1j)
z_num = np.sqrt(2)*u
z_den = pow((u/np.sqrt(2)), a)
z_intial =  z_num / z_den
b = 5 + 6

z_list = np.array([z_intial])
step = (np.sqrt(2))/(1 + 1j)

count = 0
found = False
while not found:
    

    z_pos = z_list[count]
    z_pos_nPlus1 = z_pos/step
    
    z_list = np.append(z_list, z_pos_nPlus1 )
    new_mean = np.mean(z_list)

    if new_mean == mean_of_z:

        found = True
        print(f'found at step {count}')
    else:
        count +=1
        
        

    if count == 1000:
        
        #print('nope')
        break
#print(new_mean)






print(z_intial)