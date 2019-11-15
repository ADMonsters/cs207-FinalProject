import numpy as np
from numbers import Number

from superdiff.expression import *

class add:
    def __call__(self, left, right):  # call method calls the expr method
        return self.value(left, right)
    
    @staticmethod
    def expr(left, right): # this method makes an Expression
        
        assert isinstance(left, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        assert isinstance(right, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=add)
        return node

    @staticmethod
    def value(left, right): 
  
        return left + right

    @staticmethod
    def deriv(left, right):
        try:
            left_der = left.der()   # left is an Expression object
        except:
            left_der = 0   # left is a number

        try:
            right_der = right.der()   
        except:
            right_der = 0

        result = left_der + right_der
        return result



class sub:
    def __call__(self, left, right):  # call method calls the expr method
        return self.expr(left, right)
    
    @staticmethod
    def expr(left, right): # this method makes an Expression

        assert isinstance(left, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        assert isinstance(right, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=sub)  
        return node

    @staticmethod
    def value(left, right):
        
        return left - right

    @staticmethod
    def deriv(left, right):
        try:
            left_der = left.der()   # left is an Expression object
        except:
            left_der = 0   # left is a number

        try:
            right_der = right.der()   
        except:
            right_der = 0

        result = left_der - right_der
        return result



class mul:
    def __call__(self, left, right):  # call method calls the expr method
        return self.expr(left, right)
    
    @staticmethod
    def expr(left, right):  # this method makes an Expression

        assert isinstance(left, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        assert isinstance(right, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=mul)  
        return node

    @staticmethod
    def value(left, right):
        
        return left * right

    @staticmethod
    def deriv(left, right):
        try:
            left_der = left.der()   # left is an Expression object
        except:
            left_der = 0   # left is a number

        try:
            right_der = right.der()   
        except:
            right_der = 0

        try:
            left_val = left.val()   # left is an Expression object
        except:
            left_val = left   # left is a number

        try:
            right_val = right.val()  
        except:
            right_val = right

        result = left_der * right_val + left_val * right_der 
        return result



class div():
    def __call__(self, left, right):  # call method calls the expr method
        return self.expr(left, right)
    
    @staticmethod
    def expr(left, right): # this method makes an Expression

        assert isinstance(left, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        assert isinstance(right, Variable) or isinstance(left, Number), "Not a number/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=div)  
        return node

    @staticmethod
    def value(left, right):
        try:
            left_val = left.val()   # left is an Expression object
        except:
            left_val = left   # left is a number

        try:
            right_val = right.val()  
        except:
            right_val = right

        result = left_val / right_val
        return result

    @staticmethod
    def deriv(left, right):
        try:
            left_der = left.der()   # left is an Expression object
        except:
            left_der = 0   # left is a number

        try:
            right_der = right.der()   
        except:
            right_der = 0

        try:
            left_val = left.val()   # left is an Expression object
        except:
            left_val = left   # left is a number

        try:
            right_val = right.val()  
        except:
            right_val = right

        result = (left_der * right_val - left_val * right_der) / (right_val)**2
        return result
   


def neg(something):
    '''
    unary operation that returns the negative of something
    '''
    node = Expression(0 - something)
    return node



def pos(something):
    '''
    unary operation that returns the positive of something
    '''
    node = Expression(0 + something)
    return node



class exp:
    """
    This is e to the x-th power.
    param exponent -- an Expression or a number
    """
    def __call__(self, exponent):  # call method calls the expr method
        return self.expr(exponent)
    
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Variable):  # returns an Expression

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
    def deriv(exponent):
        try:
            exponent_val = exponent.val()  
        except:
            exponent_val = exponent
            
        try:
            exponent_der = exponent.der()  
        except:
            exponent_der = 0

        result = exponent_val * exponent_der
        return result



class log():
    """
    This is natural logarithm.
    param exponent -- an Expression or a number
    """ 
    def __call__(self, exponent):  # call method calls the expr method
        return self.expr(exponent)
    
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Variable):  # returns an Expression

            node = Expression(parent1=exponent, parent2=None, operation=log)  
            return node
        
        elif isinstance(exponent, Number):  # exp(number) is just a number
            return np.log(exponent)

        else:
            raise TypeError("Not a number/Variable/Expression")

    @staticmethod
    def value(exponent):
        
        return np.log(exponent)

    @staticmethod
    def deriv(exponent):
        try:
            exponent_val = exponent.val()  
        except:
            exponent_val = exponent
            
        try:
            exponent_der = exponent.der()  
        except:
            exponent_der = 0

        result = 1 / exponent_val * exponent_der
        return result



def pow(base, exponent):
    '''
    returns an Expression
    pow(base, exponent) = exp(exponent * log(base))
    '''
    nodes = Expression(exp(exponent * log(base)))
    return nodes



class sin():
    """
    This is sine function.
    param angle -- an Expression or a number
    """ 
    def __call__(self, angle):  # call method calls the expr method
        return self.expr(angle)
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Variable):  # returns an Expression

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
    def deriv(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle
            
        try:
            angle_der = angle.der()  
        except:
            angle_der = 0

        result = np.cos(angle_val) * angle_der
        return result


class cos():
    """
    This is cosine function.
    param angle -- an Expression or a number
    """ 
    def __call__(self, angle):  # call method calls the expr method
        return self.expr(angle)
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Variable):  # returns an Expression

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
    def deriv(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle
            
        try:
            angle_der = angle.der()  
        except:
            angle_der = 0

        result = -np.sin(angle_val) * angle_der
        return result


class tan():
    """
    This is tangent function.
    param angle -- an Expression or a number
    """ 
    def __call__(self, angle):  # call method calls the expr method
        return self.expr(angle)
    
    @staticmethod
    def expr(exponent):
        if isinstance(angle, Variable):  # returns an Expression

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
    def deriv(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle
            
        try:
            angle_der = angle.der()  
        except:
            angle_der = 0

        result = 1 / np.cos(angle_val)**2 * angle_der
        return result
