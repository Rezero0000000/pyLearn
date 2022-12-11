class Student :
    # Class property
    countStudents = 0

    def __init__ (self, name, age) :
        print("Hello World")
        self.name = name
        self.age = age
        Student.countStudents += 1

re = Student("Re", 18)
ryan = Student("Ryan", 17)

print(re.__dict__)
print(Student.countStudents)

