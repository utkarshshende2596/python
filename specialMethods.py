class Employee:

    pay_raise=1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):    #  methods usually pass self(instance of class) as first parameter
        return int(self.pay * self.pay_raise)       # why self.pay_raise even if its a class varaiable.....we can use it using Emplyee.pay_raise by using selef individeual object value can be altered & by employee.pay_raise a global varaible is created

    def __repr__(self):  #represantaion of object for devlopers to understand
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)

    def __str__(self):  #readable  represantaion of object for enduser to understand
        return "{} - {}".format(self.fullname(),self.pay)

    def __add__(self, other):
        return emp_1.pay + emp_2.pay

    def __len__(self):
        return len(emp_1.first)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1)      similar to overriding of tostring() to print the content of object
#
# print(repr(emp_1))
# print(str(emp_1))
#
# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(2+3)
# print(int.__add__(2,3))
#
# print('a'+'b')
# print(str.__add__('a','b'))

# print(emp_1 + emp_2)    #overiding + operator i.e calling inbuilt __add__ function
#print(Employee.__add__(emp_1,emp_2)) #class_name.__inbuilt_funtion__.parameter

# print(len('test'))
# print("test".__len__())
# print(len(emp_1))       #len funtion is overridden to print length of name



# print(emp_1.__dict__)                           #__dict__ is used for knowing method and variable inside an object