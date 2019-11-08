class Operations():
    def add(left, right):
        expression = Expression(left, right)
        return expression

    def add_val(left, right):
        try:
            left_val = left.val   # left is an Expression object
        except:
            left_val = left   # left is a number

        try:
            right_val = right.val  
        except:
            right_val = right

        result = left_val + right_val
        return result

    def add_der(left, right):
        try:
            left_der = left.der   # left is an Expression object
        except:
            left_der = 0   # left is a number

        try:
            right_der = right.der   
        except:
            right_der = 0

        result = left_der + right_der
        return result
