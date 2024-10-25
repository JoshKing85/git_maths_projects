import numpy as np
a = 13

x = 2.9
y_num = (x-3)*(1/np.exp(x-3))
y_den = x*np.exp(-a*x)
y = y_num/y_den
print(y)



x = 3.1
y_num = (x-3)*(1/np.exp(x-3))
y_den = x*np.exp(-a*x)
y = y_num/y_den
print(y)