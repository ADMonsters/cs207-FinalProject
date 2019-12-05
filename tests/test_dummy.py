import superjacob as sj

x = sj.Var('x')
y = sj.Var('y')
z = sj.Var('z')

f = sj.make_expression(x ** 2 + y / x - sj.sin(z) / x, vars=[x, y, z])
# print(f(3, 3, 1))
print("FORWARD")
print(f.deriv(3, 3, 1))
print("REVERSE")
print(f.deriv(3, 3, 1, mode='reverse'))
