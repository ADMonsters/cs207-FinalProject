import numpy as np


class add():
    @staticmethod
    def expr(left, right, varlist):
        '''need code to rearrange the varlist'''
        
        assert isinstance(left, Expression) or isinstance(left, Variable) or isinstance(left, int) or isinstance(left, float), "Not float/int/Variable/Expression"
        assert isinstance(right, Expression) or isinstance(right, Variable) or isinstance(right, int) or isinstance(right, float), "Not float/int/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=add, varlist=varlist)
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

        result = left_val + right_val
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

        result = left_der + right_der
        return result



class sub():
    @staticmethod
    def expr(left, right):
        '''need code to rearrange the varlist'''

        assert isinstance(left, Expression) or isinstance(left, Variable) or isinstance(left, int) or isinstance(left, float), "Not float/int/Variable/Expression"
        assert isinstance(right, Expression) or isinstance(right, Variable) or isinstance(right, int) or isinstance(right, float), "Not float/int/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=sub, varlist=varlist)  
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

        result = left_val - right_val
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

        result = left_der - right_der
        return result



class mul():
    @staticmethod
    def expr(left, right):
        '''need code to rearrange the varlist'''

        assert isinstance(left, Expression) or isinstance(left, Variable) or isinstance(left, int) or isinstance(left, float), "Not float/int/Variable/Expression"
        assert isinstance(right, Expression) or isinstance(right, Variable) or isinstance(right, int) or isinstance(right, float), "Not float/int/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=mul, varlist=varlist)  
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

        result = left_val * right_val
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

        result = left_der * right_val + left_val * right_der 
        return result



class div():
    @staticmethod
    def expr(left, right):
        '''need code to rearrange the varlist'''

        assert isinstance(left, Expression) or isinstance(left, Variable) or isinstance(left, int) or isinstance(left, float), "Not float/int/Variable/Expression"
        assert isinstance(right, Expression) or isinstance(right, Variable) or isinstance(right, int) or isinstance(right, float), "Not float/int/Variable/Expression"
        
        node = Expression(parent1=left, parent2=right, operation=div, varlist=varlist)  
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
    node = Expression(0 - something, varlist=something.vars)
    return node



def pos(something):
    '''
    unary operation that returns the positive of something
    '''
    node = Expression(0 + something, varlist=something.vars)
    return node



class exp():
    """
    This is e to the x-th power.
    param exponent -- an Expression or a number
    """ 
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Expression) or isinstance(exponent, Variable):

            node = Expression(parent1=exponent, parent2=None, operation=exp, varlist=exponent.vars)  
            return node
        
        elif isinstance(exponent, int) or isinstance(exponent, float):
            return np.exp(exponent)

        else:
            raise TypeError("Not float/int/Variable/Expression")

    @staticmethod
    def value(exponent):
        try:
            exponent_val = exponent.val()  
        except:
            exponent_val = exponent

        result = np.e ** exponent_val
        return result

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
    @staticmethod
    def expr(exponent):
        if isinstance(exponent, Expression) or isinstance(exponent, Variable):

            node = Expression(parent1=exponent, parent2=None, operation=log, varlist=exponent.vars)  
            return node
        
        elif isinstance(exponent, int) or isinstance(exponent, float):
            return np.log(exponent)

        else:
            raise TypeError("Not float/int/Variable/Expression")
        

    @staticmethod
    def value(exponent):
        try:
            exponent_val = exponent.val()  
        except:
            exponent_val = exponent

        result = np.log(exponent_val)
        return result

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
    # needs to combine varlist
    nodes = Expression(exp(exponent * log(base)), varlist=varlist)
    return nodes



class sin():
    """
    This is sine function.
    param angle -- an Expression or a number
    """ 
    @staticmethod
    def expr(angle):
        if isinstance(angle, Expression) or isinstance(angle, Variable):

            node = Expression(parent1=angle, parent2=None, operation=sin, varlist=angle.vars)   
            return node
        
        elif isinstance(angle, int) or isinstance(angle, float):
            return np.sin(angle)

        else:
            raise TypeError("Not float/int/Variable/Expression")
          

    @staticmethod
    def value(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle

        result = np.sin(angle_val)
        return result

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
    @staticmethod
    def expr(angle):
        if isinstance(angle, Expression) or isinstance(angle, Variable):

            node = Expression(parent1=angle, parent2=None, operation=cos, varlist=angle.vars)   
            return node
        
        elif isinstance(angle, int) or isinstance(angle, float):
            return np.cos(angle)

        else:
            raise TypeError("Not float/int/Variable/Expression")

    @staticmethod
    def value(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle

        result = np.cos(angle_val)
        return result

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
    @staticmethod
    def expr(angle):
        if isinstance(angle, Expression) or isinstance(angle, Variable):

            node = Expression(parent1=angle, parent2=None, operation=tan, varlist=angle.vars)   
            return node
        
        elif isinstance(angle, int) or isinstance(angle, float):
            return np.tan(angle)

        else:
            raise TypeError("Not float/int/Variable/Expression")

    @staticmethod
    def value(angle):
        try:
            angle_val = angle.val()  
        except:
            angle_val = angle

        result = np.tan(angle_val)
        return result

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
