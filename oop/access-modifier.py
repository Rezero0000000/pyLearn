class Student :
    def __init__ (self, name : str, age : int, classes : str) : 
        print("Hello World")
        # Public
        self.name = name

        # Protected
        self._age = age

        # Private

        self.__classes = classes

re = Student("Re", 17, "1A")
print(re.name)
print(re._age)
# print(re.__classes) Error
