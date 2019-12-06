"""
test_expression_multivar.py

Testing multivariate autodiff and vectorized variable
"""
import pytest
import numpy as np
import superjacob as sd
from superjacob import make_expression
from superjacob.expression import *
import math


def test_Exp_multivar():
    ''' Checking multivariate functions with scalar input. '''
    
    x = Var('x')
    y = Var('y')
    
    # f = x - y
    f = make_expression(x - y * 2, vars = [x,y])
    assert f.eval(0,8) ==  -16, 'Expression evaluation error.'
    assert f.deriv(0,8, var = x) == 1, 'Expression partial derivative error.'
    assert f.deriv(0,8, var = y) == -2, 'Expression partial derivative error.'
    assert (f.deriv(0,8) == np.array([1,-2])).all, 'Expression partial derivative error.'
    
def test_Exp_eval():
    ''' Checking eval method in class Expression with vectorized inputs. '''
    x = Var('x')
    y = Var('y')
    
    # f = [-1,3] + x
#    f = make_expression([1,3] + x, vars = [x])
#    assert f.eval([2,4]) ==  [3,7], 'Expression evaluation error.'
#    
#    try:
#        f.eval(4)
#    except TypeError :
#        pass
#    except:
#        raise Exception('Did not raise error when variable has wrong dimension.')
#    

    # f = x - y
    f = make_expression(x - y, vars = [x,y])
    
    # x is R2, y is R1
    xval = np.array([2,4])
    yval = 1
    assert (f.eval(xval, yval) ==  np.array([1,3]) ).all(), 'Expression evaluation error.'
    # x is R2, y is R2
    xval = np.array([2,4])
    yval = np.array([2,4])
    assert (f.eval(xval, yval) ==  np.array([0,0]) ).all(), 'Expression evaluation error.'
    #x is R2, y is R4, should raise error
    xval = np.array([2,4])
    yval = np.array([2,4,0,0])
    try:
        f.eval(xval, yval)
    except ValueError:
        pass
    except:
        raise 
    
    # Should raise error when wrong number of arguments were provided
    try:
        f.eval(4)
    except AssertionError:
        pass
    except:
        raise Exception('Did not raise error when eval parameter has wrong number of arguments, not multivariate')

    # Should raise error when parameter is a length-one array
    try:
        f.eval([4],[4,5])
    except TypeError as msg:
        print(msg)
    except:
        raise Exception('Did not raise error when eval parameter has wrong type of arguments, wrong dimension')

#test_Exp_eval()
def test_Exp_deriv_arguments():
    ''' Checking deriv method in class Expression with vectorized inputs. 
        The test cases check the arguments passed in for deriv method. '''
    x = Var('x')
    y = Var('y')
    # f = 2x - y, x is R2, y is R1
    f = make_expression(2 * x - y, vars = [x,y])
    
    with pytest.raises(AssertionError):
        assert f.deriv(4, var = x)

    with pytest.raises(AssertionError):
        assert f.deriv(4,[4,5], var = x)

    with pytest.raises(AssertionError):
        assert f.deriv([4],[4,5], var = x)


def test_Exp_deriv_forward():
    ''' Checking deriv method in class Expression with vectorized inputs. 
        The test cases check the derivation value with forward mode. '''
    x = Var('x')
    y = Var('y')
    
    # f = [-1,3] + x
#    f = make_expression([-1,3] + x, vars = [x])
#    assert f.deriv(2) ==  1, 'Expression derivative error.'
#    assert f.deriv(0) ==  1, 'Expression derivative error.'
#    
    # f = 2x - y, x is R2, y is R1
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = 1
    
    assert (f.deriv(xval, yval, var = x) ==  [2,2]).all() , 'Expression derivation error.'
    assert f.deriv(xval, yval, var = y) ==  -1, 'Expression derivation error.'
    #print(f.deriv(xval, yval))
    print(f.deriv(xval, yval))
    assert (f.deriv(xval, yval) ==  np.array([2,2,-1]) ).all(), 'Expression derivation error.'
    
    # f = 2x - y, x is R2, y is R2
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = np.array([-2,-4])
    assert (f.deriv(xval, yval, var = x) ==  np.array([2,2])).all() , 'Expression derivation error.'
    assert (f.deriv(xval, yval, var = y) ==  np.array([-1,-1])).all(), 'Expression derivation error.'
    assert (f.deriv(xval, yval) ==  np.array([2,2,-1,-1]) ).all(), 'Expression derivation error.'
    
    # f = 2x - y, x is R2, y is R4
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = np.array([-2,-4,0,1])
    try:
        f.deriv(xval, yval, var = x)
    except TypeError as msg:
        print(msg)
        # TODO: replace message
        if msg != 'message':
            raise
    except:
        raise
        
    # f = 2x - y, x is R2, y is R1
    # TODO: sd.sum()
    # sd.dot()
    #f = make_expression(sd.sum(x) - y, vars = [x,y])
    
def test_Exp_deriv_reverse():
    ''' Checking deriv method in class Expression with vectorized inputs. 
        The test cases check the derivation value with forward mode. '''
    x = Var('x')
    y = Var('y')
    
    # f = [-1,3] + x
#    f = make_expression([-1,3] + x, vars = [x])
#    assert f.deriv(2) ==  1, 'Expression derivative error.'
#    assert f.deriv(0) ==  1, 'Expression derivative error.'
#    
    # f = 2x - y, x is R2, y is R1
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = 1
    assert (f.deriv(xval, yval, mode='reverse', var = x) ==  np.array([2,2])).all() , 'Expression derivation error.'
    assert f.deriv(xval, yval, mode='reverse', var = y) ==  -1, 'Expression derivation error.'
    #print(f.deriv(xval, yval))
    assert (f.deriv(xval, yval, mode='reverse') ==  np.array([2,2,-1]) ).all(), 'Expression derivation error.'
    
    # f = 2x - y, x is R2, y is R2
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = np.array([-2,-4])
    assert (f.deriv(xval, yval, mode='reverse',var = x) ==  np.array([2,2])).all() , 'Expression derivation error.'
    assert (f.deriv(xval, yval, mode='reverse',var = y) ==  np.array([-1,-1])).all(), 'Expression derivation error.'
    assert (f.deriv(xval, yval, mode='reverse',) ==  np.array([2,2,-1,-1]) ).all(), 'Expression derivation error.'
    
    # f = 2x - y, x is R2, y is R4
    f = make_expression(2 * x - y, vars = [x,y])
    xval = np.array([2,4])
    yval = np.array([-2,-4,0,1])
    try:
        f.deriv(xval, yval, mode='reverse',var = x)
    except TypeError as msg:
        print(msg)
        # TODO: replace message
        if msg != 'message':
            raise
    except:
        raise