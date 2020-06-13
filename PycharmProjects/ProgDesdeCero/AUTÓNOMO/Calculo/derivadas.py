from sympy import cos, sin, symbols, exp, diff, pi, euler
import symbol

x = symbols('x')
#
r = diff((x**3*cos(x) + exp(x)) / (sin(x) + 3), x)
print(r)
print()

a = diff(((sin(x)**2) / x), x)
print(a)

