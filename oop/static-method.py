class Student :
    __countStudent = 0

    def __init__ (self, name) :
        self.name = name
        Student.__countStudent += 1

    @staticmethod
    def sayHello () :
        print("Hello World")

    @classmethod 
    def getCountStudent(cls) :
        print(cls.__countStudent)

re = Student("Re")

Student.getCountStudent()
Student.sayHello()
