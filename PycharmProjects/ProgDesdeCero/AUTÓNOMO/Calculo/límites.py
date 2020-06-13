from sympy import limit, oo, sqrt, exp, log, sin, cos, tan, pi, symbols
import math


x = symbols('x')


# limite = limit(cos(1 / x), x, 0, dir="+")
# print(limite)

limite = limit(((x ** .5) - (7 ** .5)) / (x - 7), x, 7)

print(limite)

print((1 / (2 * (7 ** .5))))


