class add:
    def __call__(self, x, y): 
        return self.__class__.__name__.value(x,y)
    
    @staticmethod
    def value(x, y): 
        return x + y

# this works

obj = add()
answer = obj(1,2)

# this works

answer = add.value(1,2)

# this does not work

try:
    answer = add(1,2)
except:
    print('fail')
