import pytest
import numpy as np
import math

from superjacob.operations import *
from superjacob.expression import *
from superjacob.superjacob import *

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
    assert np.all(f_add.deriv(1,3) == [1,1])

def test_sub_expr():
    f_sub = Expression(x, y, Sub, [x, y])
    assert f_sub.eval(3,1) == 2
    assert np.all(f_sub.deriv(3,1) == [1,-1])

def test_add_expr3():
    f_add3 = make_expression(x+x+x, vars=[x])
    assert f_add3.eval(1) == 3
    assert f_add3.deriv(1) == 3
    assert f_add3.deriv(1, mode='reverse') == 3

def test_mul_expr():
    f_mul = make_expression(-2*x, vars=[x])
    assert f_mul.eval(2) == -4
    assert f_mul.deriv(2) == -2
    f_mul.deriv(2, mode='reverse') == -2

def test_mul_const_expr():
    f_mul2 = make_expression(2*x + 1, vars=[x])
    assert f_mul2.eval(5) == 11
    assert f_mul2.deriv(5) == 2
    assert f_mul2.deriv(5, mode='reverse') == 2

def test_mul_expr_stress():
    f_mul3 = make_expression(2*log(x)+1, vars=[x])
    assert f_mul3.eval(np.e) == 3
    assert f_mul3.deriv(np.e) == 2/np.e
    assert f_mul3.deriv(np.e, mode='reverse') - 2/np.e < 1e-5

def test_div_expr():
    f_div = make_expression(x/5, vars=[x])
    assert f_div.eval(5) == 1
    assert f_div.deriv(5) == 1/5
    assert f_div.deriv(5, mode='reverse') == 1/5

def test_div_const_expr():
    f_div2 = make_expression(2/x + 2, vars=[x])
    assert f_div2.eval(2) == 3
    assert f_div2.deriv(2) == -1/2
    assert f_div2.deriv(2, mode='reverse') == -1/2

def test_div_expr_stress():
    f_div3 = make_expression(2/sin(x) + 3/cos(x), vars=[x])
    assert f_div3.eval(np.pi/6) == (2/np.sin(np.pi/6)) + (3/np.cos(np.pi/6))
    assert f_div3.deriv(np.pi/6) - (-2*(1/np.tan(np.pi/6))*(1/np.sin(np.pi/6))) - (3*(1/np.cos(np.pi/6))*np.tan(np.pi/6)) < 1e-3
    assert f_div3.deriv(np.pi/6, mode='reverse') - (-2*(1/np.tan(np.pi/6))*(1/np.sin(np.pi/6))) - (3*(1/np.cos(np.pi/6))*np.tan(np.pi/6)) < 1e-3

def test_pow_expr():
    f_pow = make_expression(x**2, vars=[x])
    assert f_pow.eval(5) == 25
    assert f_pow.deriv(5) == 10
    assert f_pow.deriv(5, mode='reverse') == 10

def test_pow_stress():
    f_pow_stress = make_expression(x**(sin(x)), vars=[x])
    assert f_pow_stress.eval(np.pi / 6) == (np.pi / 6)**(1/2)
    assert f_pow_stress.deriv(np.pi / 6) == ((np.sin(np.pi / 6) / (np.pi / 6)) + np.log(np.pi / 6)*np.cos(np.pi / 6))*(np.pi / 6)**(1/2)
    assert float(f_pow_stress.deriv(np.pi/6, mode='reverse')) - ((np.sin(np.pi / 6) / (np.pi / 6)) + np.log(np.pi / 6)*np.cos(np.pi / 6))*(np.pi / 6)**(1/2) < 1e-6
    
    # Edge case when f = x1^x2 and x1 < 0
    f_pow_edge = make_expression(cos(x)**2, vars=[x])
    assert f_pow_edge.deriv(np.pi/3) - (-2*np.cos(np.pi/3)*np.sin(np.pi/3)) < 1e-6
    assert f_pow_edge.deriv(np.pi) - (-2*np.cos(np.pi)*np.sin(np.pi)) < 1e-6
    assert f_pow_edge.deriv(np.pi, mode='reverse') - (-2*np.cos(np.pi)*np.sin(np.pi)) < 1e-3

def test_log_expr():
    # Natural log -- default
    f_nlog = make_expression(log(x), vars=[x])
    assert f_nlog.eval(np.e) == 1
    assert f_nlog.deriv(np.e) == 1/np.e
    assert f_nlog.deriv(np.e, mode='reverse') - 1/np.e < 1e-6

    # Custom log -- base 10
    f_tlog = make_expression(log(x, 10), vars=[x])
    assert f_tlog.eval(100) == 2
    assert f_tlog.deriv(100) == 1 / (100*np.log(10))
    assert f_tlog.deriv(100) == 1 / (100*np.log(10))
    assert float(f_tlog.deriv(100, mode='reverse')) == 1 / (100*np.log(10))

# Multivariate functions
z = Var("z")
w = Var("w")
def test_multi():
    fm1 = make_expression((x+y+z)**2, vars=[x,y,z])
    assert fm1.eval(2,3,4) == 81
    assert np.allclose(fm1.deriv(2,3,4), np.array([18.0,18.0,18.0]))
    assert fm1.deriv(2,3,4, var=z) - 18 < 1e-6 # Partial derivative

    fm2 = make_expression(sin(x) + cos(y), vars=[x,y])
    assert fm2.eval(np.pi, np.pi) - -1 < 1e-6
    assert np.allclose(fm2.deriv(np.pi, np.pi), np.array([-1, 0]))

    # f = ((w * sin(x)) + (z * cos(y))) / (w * z)^2
    # f = h / g
    fm3 = make_expression((w*sin(x)+z*cos(y))/(w*z)**2, vars=[x,y,z,w])
    h = (5 * np.sin(np.pi)) + (3 * np.cos(np.pi))
    g = (3*5)**2
    assert fm3.eval(np.pi, np.pi, 3, 5) == ((5 * np.sin(np.pi)) + (3 * np.cos(np.pi))) / (3*5)**2
    fm3_jacobx = g*(5*np.cos(np.pi)) / g**2
    fm3_jacoby = g*(-3*np.sin(np.pi)) / g**2
    fm3_jacobz = ((g*np.cos(np.pi)) - (h*2*(5**2)*3)) / g**2
    fm3_jacobw = ((g*np.sin(np.pi)) - (h*2*(3**2)*5)) / g**2
    assert np.allclose(fm3.deriv(np.pi, np.pi, 3, 5), np.array([fm3_jacobx, fm3_jacoby, fm3_jacobz, fm3_jacobw]))

# Vector valued functions
def test_vectors():
    fv1 = make_expression(x+y, x-y, vars=[x,y])
    assert fv1.eval(5, 4) == [9, 1]
    assert fv1.deriv(5, 4) == [[1,1],[1,-1]]

    fv2 = make_expression(2*x+y, x-2*y, y+z, vars=[x,y,z])
    assert fv2.eval(10,11,12) == [31, -12, 23]
    assert fv2.deriv(10, 11, 12) == [[2,1,0],[1,-2,0],[0,1,1]]

    # f = [e^(sin(x+y)), tan(y) + sin(z), 2*log(w) + (xy)^2]
    fv3 = make_expression(exp(sin(x+y)), tan(y) + sin(z), 2*log(w) + (x*y)**2, vars=[x,y,z,w])
    assert fv3.eval(np.pi/4, np.pi/4, np.pi/3, 5) == [np.exp(np.sin(np.pi/4 + np.pi/4)), np.tan(np.pi/4) + np.sin(np.pi/3), 2*np.log(5) + (np.pi/4*np.pi/4)**2]
    fv3_df1 = [np.exp(np.sin(np.pi/2))*np.cos(np.pi/2), np.exp(np.sin(np.pi/2))*np.cos(np.pi/2), 0, 0]
    fv3_df2 = [0, 1/(np.cos(np.pi/4)**2), np.cos(np.pi/3), 0]
    fv3_df3 = [2*np.pi/4*(np.pi/4)**2, 2*np.pi/4*(np.pi/4)**2, 0, 2/5]
    assert fv3.deriv(np.pi/4, np.pi/4, np.pi/3, 5) == [fv3_df1, fv3_df2, fv3_df3]

def test_ops_reverse():
    assert Add.reverse(x.eval(3), x.deriv(3), y.eval(2), y.deriv(2)) == (1,1)
    assert Sub.reverse(x.eval(3), x.deriv(3), y.eval(2), y.deriv(2)) == (1,-1)
    assert Mul.reverse(x.eval(3), y.eval(2)) == (2,3)


# Diabolical function
def test_diabolical():
    # fd1 = (x^(sin(x^2))) / (e^(tan(x)))
    fd1 = make_expression((x**sin(x**2))/(exp(x**tan(x))), vars=[x])
    assert fd1.eval(np.pi) == (np.pi**np.sin((np.pi)**2))/np.exp(np.pi**np.tan(np.pi))
    # num1 = np.pi**(np.sin(np.pi**2)-1)
    # num2 = np.sin(np.pi**2) + (2*(np.pi**2)*np.cos(np.pi**2)*np.log(np.pi)) - (np.pi*(1/np.cos(np.pi)**2))
    # denom = np.exp(np.tan(np.pi))
    # assert fd1.deriv(np.pi) == (num1*num2)/denom
    
# Types
string_a = "H"
string_b = "I"
random_list = [1, 3, "H"]
def test_types():
    with pytest.raises(TypeError):
        add(string_a, string_b)
    with pytest.raises(TypeError):
        sub(string_a, string_b)
    with pytest.raises(TypeError):
        mul(string_a, string_b)
    with pytest.raises(TypeError):
        div(string_a, string_b)
    with pytest.raises(TypeError):
        div(string_a, random_list)
    

