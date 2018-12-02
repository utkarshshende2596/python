def decorator_fun(outer_funtion):
    def wrapper_fun():
        print(" wrapper Before calling in {}".format(outer_funtion.__name__))
        return outer_funtion()
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



# @decorator_class
@decorator_fun
def display():
    print("in display function")

#when we use decorator
display()
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