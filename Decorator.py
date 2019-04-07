from functools import wraps
def decorator_fun(outer_funtion):
    def wrapper_fun(*args,**kwargs):
        print(" wrapper Before calling in {}".format(outer_funtion.__name__))
        return outer_funtion(*args,**kwargs)
    return wrapper_fun

#
# def decorator_class(outer_funtion):
#     def __init__(self,outer_funtion):
#         self.outer_funtion = outer_funtion
#
#     def __call__(self):
#         print("class Before calling in {}".format(outer_funtion.__name__))
#         return self.outer_funtion()
#
#

def test_dec(viewfunction):
    @wraps(viewfunction)
    def wrapper(*args,**kwargs):
        print "inside {} with {} {}".format(viewfunction.__name__,args,kwargs)
        return viewfunction(*args,**kwargs)
    return wrapper


#@decorator_class
@test_dec
@decorator_fun
def display(arg1,arg2):
    print("in display function {}.{}".format(arg1,arg2))

#when we use decorator
display(2,'sdf')


#
# |
# |
# | - > display is equivaltent to function below
# if we dont use decorator
# display = decorator_fun(display)
# display()

# call_function = decorator_fun(display)
# call_function()

#it can be used for logging in decorator_fun() we can write logging code to trace each value inserted.
#it can also be used for logging time each function took for execution.