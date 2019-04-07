import datetime
import logging

logger = logging.getLogger(__name__)
formattor = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
logger.setLevel(logging.INFO)
filehandler = logging.FileHandler('sample.log')
filehandler.setFormatter(formattor)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formattor)
logger.addHandler(filehandler)
logger.addHandler(stream_handler)


# logging.basicConfig(filename="test.log", level=logging.INFO, format="%(levelname)s:%(message)s")


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @classmethod        #alternative for contructor  ...... this type is usuallly used in date and pre-built method
    def from_string(cls,str):   # class methods usually pass class(cls = Employee) as first parameter
        first, last, pay = str.split(',')
        logger.info("{}.{}".format(first, last))
        return cls(first,last,pay)

    @staticmethod  # if you are not using self or class inside method then make that method as static.
    def is_workday(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        return True

str1 = "utkarsh,shende,5000"
str2 = "apurva,shende,6000"

emp_1 = Employee.from_string(str2) # they pass class name automatically by default (for class method)

# print(emp_1.pay)
# print(emp_1.first+" "+emp_1.last)
date_time=datetime.date(2018, 5, 13)

# print(Employee.is_workday(date_time))

