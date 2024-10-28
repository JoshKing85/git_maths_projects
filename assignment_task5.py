import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
a = 13

x = np.linspace(-10, 10, 1000)
y_num = math.factorial(a)
y_den = x
y = -(y_num/y_den)
mpl.rcParams['font.size']=14


plt.plot(x, y, 'r--')
plt.xlim(-10, 10)



plt.grid()
plt.axhline(c='black', linewidth=1)
plt.axvline(c='blue', linestyle='--', linewidth=1)
plt.yscale('symlog') 
plt.show()


# p(a 1) is the pemuatations of a set,a is equal to number of elements a 1 is the group size.
# Permutations are the number of different orders a set can have.
# The formula for nPr is n!/(n-r)!. n is number of elements and r is the group size. As group size is 1, meaning a one digit choice and a is equal to  13. There are 13 permutations.

# We can check this answer the using formula.
perm = int((math.factorial(a))/math.factorial(a - 1))
print(perm)


# (a 1) is the combinations of a set, a is equal to number of elements a 1 is the group size. 
#Combinations are similar to permutaions but an important distiction between both is that the order of a combination does not matter. Only the selection matters.
# The formula for nCr is n!/(n-r)!r!. n is equal to the number of elements and r is equal to the group size. As the group size is 1, meaning a one digit choice and a is equal to 13. There are 13 combinations.

# We can check this answer using the math library combinations function.
comb = math.comb(a, 1)
print(comb)