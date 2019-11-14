import pytest
import numpy as np

import sys 
sys.path.append('..')

from superdiff.operations import *
from superdiff.expression import *

# Asserts to ensure correct output with basic inputs
a, b = 2, 3
node_a, node_b = Var("x"), Var("y")

def test_basic_add():
    assert add.value(a, b) == 5
    assert add.deriv(a,b) == 0
    assert add.value(node_a(4), node_b(5)) == 9
    # assert add.deriv(node_a.deriv(4), node_b.deriv(5)) == 2

def test_basic_sub():
    assert sub.value(b, a) == 1
    assert sub.deriv(b, a) == 0
    assert sub.value(node_a(5), node_b(4)) == 1
    # assert sub.deriv(node_a.deriv(4), node_b.deriv(5)) == 0

def test_basic_mul():
    assert mul.value(a, b) == 6
    assert mul.deriv(a, b) == 0
    assert mul.value(node_a(5), node_b(4)) == 20
    # assert mul.deriv(node_a.deriv(4), node_b.deriv(5)) == 1

def test_basic_div():
    assert div.value(b, a) == 1.5
    assert div.deriv(a, b) == 0
    assert div.value(node_a(1), node_b(3)) == 1/3
    # assert div.deriv(node_a(1), node_b(3)) == 2/9
    # node_a(1) returns number, so div.deriv() treats it like constant though it's a variable
    # deriv() in Expression needs to be compatible so operations don't get confused

def test_basic_exp():
    assert exp.value(a) == np.e**a
    # assert exp.deriv(node_a(2)) == np.exp(a)

def test_basic_log():
    assert log.value(a) == np.log(a)
    # assert log.deriv(node_a(1)) == 1/node_a(1)

def test_basic_pow():
    # assert pow(node_a, node_b)(2,3) == 2**3
    pass

def sin():
    assert sin.value(node_a(np.pi)) == 0

def cos():
    assert cos.value(node_a(np.pi)) == -1

def tan():
    assert tan.value(node_a(np.pi)/4) == 1

# error handling and corner cases
string_a = "H"
string_b = "I"

# def test_add_types():
#     with pytest.raises(TypeError):
#         add.value(string_a, string_b)

