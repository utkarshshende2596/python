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

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


print(emp_1.__dict__)                           #__dict__ is used for knowing method and variable inside an object