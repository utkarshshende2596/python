# class Fibo():
#     def fib(self,n):    # write Fibonacci series up to n
#         print "asasd"
#         a, b = 0, 1
#         while b < n:
#             print b,
#             a, b = b, a+b
#
#     def fib2(self,n):   # return Fibonacci series up to n
#         result = []
#         a, b = 0, 1
#         while b < n:
#             result.append(b)
#             a, b = b, a+b
#         return result
#
#     def __fib3(self,n):    # write Fibonacci series up to n
#         a, b = 0, 1
#         while b < n:
#             print b,
#             a, b = b, a+b
#
#
# def fib(n):  # write Fibonacci series up to n
#     a, b = 0, 1
#     while b < n:
#         print b,
#         a, b = b, a + b
#
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))




s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(arg)

class Foo:
    pass

# print(s)
# print(a)
# foo('quux')
# x = Foo()
# print(x)

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)

