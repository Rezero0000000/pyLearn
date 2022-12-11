class Student :
    def __init__ (self, name, age) :
        print("Hello World")
        self.name = name
        self.age = age

re = Student("Re", 18)
print(re.__dict__)


