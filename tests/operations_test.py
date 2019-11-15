import pytest
import numpy as np

from superdiff.operations import *
from superdiff.expression import *

# Asserts to ensure correct output with basic inputs
a, b = 2, 3
x, y = Var("x"), Var("y")
f = Expression(x, y, add, [x,y])

def test_basic_add():
    assert add.value(a, b) == 5
    assert add.deriv(a,b) == 0
    assert add.value(x(4), y(5)) == 9
    # assert add.deriv(x.deriv(4), y.deriv(5)) == 2

def test_add_expr():
    assert f.eval(1,3) == 4

def test_basic_sub():
    assert sub.value(b, a) == 1
    assert sub.deriv(b, a) == 0
    assert sub.value(x(5), y(4)) == 1
    # assert sub.deriv(x.deriv(4), y.deriv(5)) == 0

def test_basic_mul():
    assert mul.value(a, b) == 6
    assert mul.deriv(a, b) == 0
    assert mul.value(x(5), y(4)) == 20
    # assert mul.deriv(x.deriv(4), y.deriv(5)) == 1

def test_basic_div():
    assert div.value(b, a) == 1.5
    assert div.deriv(a, b) == 0
    assert div.value(x(1), y(3)) == 1/3
    # assert div.deriv(x(1), y(3)) == 2/9
    # x(1) returns number, so div.deriv() treats it like constant though it's a variable
    # deriv() in Expression needs to be compatible so operations don't get confused

def test_basic_exp():
    assert exp.value(a) == np.e**a
    # assert exp.deriv(x(2)) == np.exp(a)

def test_basic_log():
    assert log.value(a) == np.log(a)
    # assert log.deriv(x(1)) == 1/x(1)

def test_basic_pow():
    # assert pow(x, y)(2,3) == 2**3
    pass

def sin():
    assert sin.value(x(np.pi)) == 0

def cos():
    assert cos.value(x(np.pi)) == -1

def tan():
    assert tan.value(x(np.pi)/4) == 1

# error handling and corner cases
string_a = "H"
string_b = "I"

# def test_add_types():
#     with pytest.raises(TypeError):
#         add.value(string_a, string_b)

