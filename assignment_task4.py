import sympy as sp
import math
a = 13
x, y = sp.symbols('x y')

lhs = sp.Pow(y, 2)*((x-2)*a)
rhs = sp.Pow(x, 3) - (2*a*sp.Pow(x, 2)) + (sp.Pow(a, 2)*x)

lhs /= ((x-2)*a)
rhs /= ((x-2)*a)
# lhs is postive for all real numbers. lhs = rhs therefore, rhs > 0 for all real numbers.
# Too solve for x, rhs = 0.
equation = sp.Eq(rhs, 0)
solution = sp.solve(equation)
print(solution)





