class Dog:
    def __init__(self,breed,age):
 #       self.name = breed
        self.age = age

    @classmethod
    def count(cls,desc):
        name,age=desc.split(",")
        return cls(name,age)

    @staticmethod
    def house():
        pass



a=Dog.count('labra,23')

# b = a.house()

print a.__dict__
print getattr(a,'name','done')

# print Dog('labra',34)
