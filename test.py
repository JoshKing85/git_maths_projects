import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
a = 13
mpl.rcParams['font.size']=12

x = np.linspace(-10, 40, 1000)
y = np.sqrt((x**3 - 13*x*(2*x - 13))/(x -2*a)**2)
asymptote = 26


fig = plt.figure(figsize=(8, 8))
plt.plot(x, y, 'k--', label=r'$\sqrt{\frac{x^3 - 13x(2x - 13)}{(x - 2a)^2}}$')
plt.axvline(x=asymptote, color='red', linestyle='--', label='Asymptote at $x = 26$')
plt.grid()
plt.xlim(-1, 40)
plt.ylim(0, 40)

plt.legend(loc='upper left', fontsize=12, )
plt.xlabel('x')
plt.ylabel('y ', rotation= 0)


plt.axhline(c='black', linewidth= 1.1)
plt.axvline(c= 'black', linewidth= 1.1)
plt.plot(x, y, 'k--')


plt.xticks(np.arange(0, 40, 13))
plt.show()