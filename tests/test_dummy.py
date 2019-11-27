import superdiff as sd

x = sd.Var('x')
y = sd.Var('y')
z = sd.Var('z')

f = sd.make_expression(x ** 2 + y / x - sd.sin(z) / x, vars=[x, y, z])
print(f(3, 3, 1))
print(f.deriv(3, 3, 1))