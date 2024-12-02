import sympy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

a = 13  #We are group number 13 and a is equal to group number.

# Using sympy initialize x,y as mathamatical symbols.
x, y = sp.symbols('x y')

# Intialize left hand side(lhs) and right hand side(rhs).
lhs = sp.Pow(y, 2)*sp.Pow((x-2*a), 2)
rhs = sp.Pow(x, 3) - a*x*(2*x - a)

# Manipulate both and divide through by (x-2a)*2 
lhs = (lhs/sp.Pow((x-2*a), 2))
rhs = (rhs/sp.Pow((x-2*a), 2))

# Take the square root of both sides, thereby converting the equation into an explicit form.
lhs = sp.sqrt(lhs)
rhs = sp.sqrt(rhs)

# Initialize 
eq = sp.Eq(lhs, rhs)
print('The explicit form =') 
sp.pprint(eq)

# As we want x values for domain, take the square root of rhs.
rhs = sp.Pow(rhs, 2)

# Equate expression to 0, as rhs must > 0 for all real numbers and solve for the roots.
roots = sp.solve(rhs, x)
print('The roots for f(x) are')
for i in roots:
    print(f'x = {i}')

# Show asymptote using denominator.
denominator = (x - 26)**2
asymptote= sp.Eq(denominator, 0)

# Solve the equation to find where the denominator equals zero.
asymptote_x = sp.solve(asymptote_condition, x)
asymptote_x = asymptote_x[0]
print(f"Vertical asymptote at x = {asymptote_x}")

# Verify x values are real when x > 26
verify = rhs.subs(x, 26.1)
print(f'Verify f(x) is real for x > 26. When x = 26.1 f(x) = {verify}')

#As x value greater than 0 and aymptote at 26 the domain is ...
domain =  r"$\text{Domain = } [0, 26) \cup (26, 39]$"
sp.init_printing()  
display(Latex(domain))





