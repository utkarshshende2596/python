# import import_module
# print help(import_module)
# print dir(import_module)
# print import_module.__name__
from import_module import Fibo as a
# Fibo()._fib3(3)

x = a()
print dir(x)
# x._Fibo__fib3(5)

# class Foo(object):
#      def __init__(self):
#          self.__baz = 42
#      def foo(self):
#          print self.__baz
#
# class Bar(Foo):
#      def __init__(self):
#          super(Bar, self).__init__()
#          self.__baz = 21
#      def bar(self):
#          print self.__baz
#
# x = Bar()
# # print dir(x)
# # print x.__dict__
# print x.foo()


##reload
# import_module.Fibo().fib(5) #-> 1 1 2 3
# reload(import_module)
# import_module.Fibo().fib(5) #->asasd  1 1 2 3
