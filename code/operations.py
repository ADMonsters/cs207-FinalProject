import numpy as np

## Assume our Expression class looks like this
class Expression():
    def __init__(self, p1, p2=None, operation="string", varlist):
        self.p1 = p1
        self.p2 = p2
        self.operation = operation
        for i in varlist:
            "Assign variables"

    def val(self):
        eval(self.operation + ".value(self.p1, self.p2)") # eval() calls an Operation
        "..."
        pass

    def der(self):
        "..."
        pass

    def __add__(self, other):
        "recompile the varlist"
        pass

    def forward(self, value_input):
        "Assign values to variables"
        pass



class BaseOperation():


class Add(BaseOperation):
    @staticmethod
    def expr(left, right, varlist):
        node = Expression(p1=left, p2=right, operation="Add", varlist)  
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

class Sub(BaseOperation):
    @staticmethod
    def expr(left, right):
        node = Expression(left, right, "Sub", varlist)  
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

class Mul(BaseOperation):
    @staticmethod
    def expr(left, right):
        node = Expression(left, right, "Mul", varlist)  
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

        result = left_der * right.val() + left.val() * right_der 
        return result
