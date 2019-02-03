class Employee:

    pay_raise=1.05
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property           #similar to getter u don't need to make a funtion call ...can directly access using property name
    def email(self):
       return '{}.{}@email.com'.format(self.first,self.last)

    @property       #getter
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter                #setter(getter_function.setter)
    def fullname(self,name):
        first, last = name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print('Delete Funtion')
        self.first = None
        self.last = None


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_1.fullname='Corey anderson'     #if setter is not made this line would not work


print(emp_1.email)


print("form testing purpose111jk")

jkh
dsfjhfdkhkdsfkjhfdgit
print("form testing purpose111jk")print("form testing purpose111jk")print("form testing purpose111jk")print("form testing purpose111jk")



