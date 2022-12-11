class Student :
    countStudent = 0

    def __init__ (self, name) :
        self.name = name
        self.countStudent += 1
    
    @staticmethod
    def sayHello () :
        print("Hello World")

    @staticmethod 
    def getCountStudent(cls) :
        print(cls.countStudent)

Student.getCountStudent()
Student.sayHello()
