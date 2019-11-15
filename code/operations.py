import numpy as np
from numbers import Number
from superdiff import Var

def checktype(x):
    '''
    raises error if the input is not a number/Variable/Expression
    '''
    assert isinstance(x, Var) or isinstance(x, Number), "Not a number/Variable/Expression"


class add():
    
    @staticmethod
    def expr(left, right): # this method makes an Expression       
        checktype(left)
        checktype(right)
        
        node = Expression(parent1=left, parent2=right, operation=add)
        return node

    @staticmethod
    def value(left, right): 
  
        return left + right

    @staticmethod
    def deriv(left, right):
        
        return left_der + right_der


class sub(Binary):
    
    @staticmethod
    def expr(left, right): # this method makes an Expression
        checktype(left)
        checktype(right)
        
        node = Expression(parent1=left, parent2=right, operation=sub)  
        return node

    @staticmethod
    def value(left, right):
        
        return left - right

    @staticmethod
    def deriv(left_der, right_der, left_val, right_val):

        return left_der - right_der


class mul():
    
    @staticmethod
    def expr(left, right):  # this method makes an Expression
        checktype(left)
        checktype(right)
        
        node = Expression(parent1=left, parent2=right, operation=mul)  
        return node

    @staticmethod
    def value(left, right):
        
        return left * right

    @staticmethod
    def deriv(left_der, right_der, left_val, right_val):

        result = left_der * right_val + left_val * right_der 
        return result


class div():
    
    @staticmethod
    def expr(left, right): # this method makes an Expression
        checktype(left)
        checktype(right)
        
        node = Expression(parent1=left, parent2=right, operation=div)  
        return node

    @staticmethod
    def value(left, right):

        return left / right

    @staticmethod
    def deriv(left_der, right_der, left_val, right_val):

        result = (left_der * right_val - left_val * right_der) / (right_val)**2
        return result
   


def neg(expression):
    '''
    unary operation that returns the negative of something
    '''
    return 0 - expression



def pos(expression):
    '''
    unary operation that returns the positive of something
    '''
    return 0 + expression


class log():
    """
    This is natural logarithm.
    param exponent -- an Expression or a number
    """ 
    
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Var):  # returns an Expression

            node = Expression(parent1=exponent, parent2=None, operation=log)  
            return node
        
        elif isinstance(exponent, Number):  # log(number) is just a number
            return np.log(exponent)

        else:
            raise TypeError("Not a number/Variable/Expression")

    @staticmethod
    def value(exponent):
        
        return np.log(exponent)

    @staticmethod
    def deriv(exponent_der, exponent_val):

        result = 1 / exponent_val * exponent_der
        return result

class exp():
    """
    This is e to the x-th power.
    param exponent -- an Expression or a number
    """
    
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Var):  # returns an Expression

            node = Expression(parent1=exponent, parent2=None, operation=exp)  
            return node
        
        elif isinstance(exponent, Number):  # exp(number) is just a number
            return np.exp(exponent)

        else:
            raise TypeError("Not a number/Variable/Expression")

    @staticmethod
    def value(exponent):
        
        return np.e ** exponent

    @staticmethod
    def deriv(exponent_der, exponent_val):

        result = exponent_val * exponent_der
        return result


def pow(base, exponent):
    '''
    returns an Expression
    pow(base, exponent) = exp(exponent * log(base))
    '''
    nodes = Expression(exp.expr(exponent * log.expr(base)))
    return nodes



class sin():
    """
    This is sine function.
    param angle -- an Expression or a number
    """ 
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Var):  # returns an Expression

            node = Expression(parent1=angle, parent2=None, operation=sin)  
            return node
        
        elif isinstance(angle, Number):  # exp(number) is just a number
            return np.sin(angle)

        else:
            raise TypeError("Not a number/Variable/Expression")
          

    @staticmethod
    def value(angle):
        
        return np.sin(angle)

    @staticmethod
    def deriv(angle_der, angle_val):

        result = np.cos(angle_val) * angle_der
        return result


class cos():
    """
    This is cosine function.
    param angle -- an Expression or a number
    """ 
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Var):  # returns an Expression

            node = Expression(parent1=angle, parent2=None, operation=cos)  
            return node
        
        elif isinstance(angle, Number):  # exp(number) is just a number
            return np.cos(angle)

        else:
            raise TypeError("Not a number/Variable/Expression")

    @staticmethod
    def value(angle):
        
        return np.cos(angle)

    @staticmethod
    def deriv(angle_der, angle_val):

        result = -np.sin(angle_val) * angle_der
        return result


class tan():
    """
    This is tangent function.
    param angle -- an Expression or a number
    """ 
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Var):  # returns an Expression

            node = Expression(parent1=angle, parent2=None, operation=tan)  
            return node
        
        elif isinstance(angle, Number):  # exp(number) is just a number
            return np.tan(angle)

        else:
            raise TypeError("Not a number/Variable/Expression")

    @staticmethod
    def value(angle):
        
        return np.tan(angle)

    @staticmethod
    def deriv(angle_der, angle_val):

        result = 1 / np.cos(angle_val)**2 * angle_der
        return result
