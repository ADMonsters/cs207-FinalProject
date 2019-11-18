import pytest
import numpy as np
import math

from superdiff.operations import *
from superdiff.expression import *
from superdiff.superdiff import *

# Asserts to ensure correct output with basic inputs
a, b = 2, 3
x, y = Var("x"), Var("y")

def test_basic_add():
    assert Add.eval(a, b) == 5
    assert Add.deriv(a, 0, b, 0) == 0
    assert Add.eval(x(4), y(5)) == 9
    assert Add.deriv(x.eval(3), x.deriv(3), y.eval(2), y.deriv(2)) == 2

def test_basic_sub():
    assert Sub.eval(b, a) == 1
    assert Sub.deriv(b, 0, a, 0) == 0
    assert Sub.eval(x(5), y(4)) == 1
    assert Sub.deriv(x.eval(3), x.deriv(2), y.eval(3), y.deriv(3)) == 0

def test_basic_mul():
    assert Mul.eval(a, b) == 6
    assert Mul.deriv(a, 0, b, 0) == 0
    assert Mul.eval(x(5), y(4)) == 20
    assert Mul.deriv(x.eval(2), x.deriv(2), y.eval(3), y.deriv(3)) == 5

def test_basic_div():
    assert Div.eval(b, a) == 1.5
    assert Div.deriv(a, 0, b, 0) == 0
    assert Div.eval(x(1), y(3)) == 1/3
    assert Div.deriv(x.eval(4), x.deriv(4), y.eval(2), y.deriv(2)) == -1/2

def test_basic_pow():
    assert Pow.eval(a, b) == 8
    assert Pow.deriv(a, 0, b, 0) == 0
    assert Pow.eval(x.eval(2), y.eval(2)) == 4
    # Derivative of x^3 --> 3x^2 --> evaluate at x = 4 --> 48
    assert math.ceil(Pow.deriv(x.eval(4), x.deriv(4), 3, 0)) == 48

def test_basic_exp():
    assert Exp.eval(a) == np.exp(a)
    assert Exp.deriv(a, 0) == 0
    assert Exp.eval(x.eval(3)) == np.exp(3)
    assert Exp.deriv(x.eval(3), x.deriv(3)) == np.exp(3)

def test_basic_nlog():
    assert NLog.eval(a) == np.log(a)
    assert NLog.deriv(a, 0) == 0
    assert NLog.eval(x(1)) == np.log(x(1))
    assert NLog.deriv(x(1), x.deriv(1)) == 1/x(1)

def test_basic_log():
    assert Log.eval(b, a) == np.log(b) / np.log(a) 
    assert Log.deriv(b, 0, a, 0) == 0
    assert Log.eval(x(2), x(10)) == np.log(2) / np.log(10)
    assert Log.deriv(x.eval(10), x.deriv(10), 2, 0) == 1 / (10 * np.log(2))

def test_basic_sin():
    assert math.floor(Sin.eval(x(np.pi))) == 0
    assert Sin.deriv(x(np.pi), x.deriv(np.pi)) == -1

def test_basic_cos():
    assert math.floor(Cos.eval(x(np.pi))) == -1
    assert math.ceil(Cos.deriv(x(np.pi), x.deriv(np.pi))) == 0

def test_basic_tan():
    assert math.ceil(Tan.eval(x(np.pi)/4)) == 1
    assert math.ceil(Tan.deriv(x(np.pi/3), x.deriv(np.pi/3))) == 4

def test_add_expr():
    f_add = Expression(x, y, Add, [x, y])
    assert f_add.eval(1,3) == 4
    assert f_add.deriv(1,3) == (1,1)

def test_sub_expr():
    f_sub = Expression(x, y, Sub, [x, y])
    assert f_sub.eval(3,1) == 2
    assert f_sub.deriv(3,1) == (1,-1)

z = Var("z")
# f_add3 = Expression(x+y, z, Add, [x,y,z])
def test_add_expr3():
    f_add3 = make_expression(x+x+x, vars=[x])
    assert f_add3.eval(1) == 3
    assert f_add3.deriv(1) == 3

def test_mul_expr():
    f_num = make_expression(-2*x, vars=[x])
    assert f_num.eval(2) == -4
    assert f_num.deriv(2) == -2

def test_mul_const_expr():
    f_num2 = make_expression(2*x + 1, vars=[x])
    assert f_num2.eval(5) == 11
    assert f_num2.deriv(5) == 2

def test_pow_expr():
    f_pow = make_expression(x**2, vars=[x])
    assert f_pow.eval(5) == 25
    assert f_pow.deriv(5) == 10

def test_pow_stress():
    f_pow_stress = make_expression(x**(sin(x)), vars=[x])
    assert f_pow_stress.eval(np.pi / 6) == (np.pi / 6)**(1/2)

# def test_sin():
    



# Diabolical functions


# error handling and corner cases
string_a = "H"
string_b = "I"

# def test_add_types():
#     with pytest.raises(TypeError):
#         add.value(string_a, string_b)

