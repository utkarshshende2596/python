class Employee:
    def __init__(self,first,last):      #constructor
        self.first=first
        self.last=last

    def full_name(self):                #constructor and methods require self(instance of class) as a parameter as mandate
        return self.first+" "+self.last


emp_1 = Employee('utkarsh','shende')
emp_1.full_name() #1
Employee.full_name(emp_1) #1 is converted into this therefore self as a parameter needs to be passed