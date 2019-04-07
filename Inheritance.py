class Employee:
    raise_amt=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.fullname=first+" "+last
        self.pay=pay


    def pay_amt(self):
        return self.pay * self.raise_amt


class Devloper(Employee): #inheritance
    raise_amt = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super(object).__init__(first,last,pay)    # call to constructor of employee
        # Employee.__init__(first,last,pay)  is same as above but is usally used in multiple inheritance
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super(object).__init__(first, last, pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_employee(self):
        for emp in self.employee:
            print(emp.fullname)






emp_1 = Employee('utkarsh','shende',1000)
emp_2 = Devloper('utkarsh1','shende1',1001,'Java')

man_1 = Manager('apurva','shende',2202,[emp_1,emp_2])
man_1.print_employee()

# print(isinstance(man_1,Employee))  to check object is instance of specific class
# print(issubclass(Devloper,Employee)) to check subclass
# print(emp_2.__dict__)

# print(emp_1.pay)
# emp_1.pay = emp_1.pay_amt()
# print(emp_1.pay)
#print(emp_1.first+" "+emp_1.last)
# print(help(Manager))


#Conventional method takes less time than getattr(), but when default values have to be used in case of missing attributes, getattr() is a good choice.
#Applications : The are many applications of getattr(), few of them already mentioned in cases of absence of attributes of objects, in web developments where some of form attributes are optional. Also useful in cases of Machine Le