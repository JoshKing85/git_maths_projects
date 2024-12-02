# Initialize numerator and denominator in x,y variable.
a = 13
x = np.linspace(-10000, 10000, 100000)
y_num = math.factorial(a)
y_den = x
#Intialize y, preventing division of 0.
y = np.where(x != 0, -(y_num / y_den), np.nan)

#Define figure size.Plot graph inputing x,y. 
mpl.rcParams['font.size']=14
fig = plt.figure(figsize=(6, 6))

#Plot graph inputing x,y and asymptote
plt.plot(x, y, 'r--', label=r'$f(x) = \frac{13!}{x}$')
plt.axvline(0, color='blue', linestyle='--', linewidth=1, label='Asymptote at $x = 0$')

plt.xlim(-10000, 10000)

#Label and define graph.
plt.legend(loc='upper right', fontsize=10)
plt.xlabel('x')
plt.ylabel('y (logscale)', rotation= 0)
plt.grid()
plt.axhline(c='black', linewidth=1)
plt.axvline(c='blue', linestyle='--', linewidth=1)
plt.yscale('symlog') 
plt.yticks([1e10, 1e8, 1e6, 1e4, 1e2, 0, -1e2, -1e4, - 1e6, - 1e8, -1e10 ])
plt.show()