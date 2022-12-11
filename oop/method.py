class Student :
    def __init__ (self, name, age) :
        print("Hello World")
        self.name = name
        self.age = age

    def incrementAge (self) :
        self.age += 1
        return self.age

    def sayWaifu (self) :
        print(f"Rem sayang banget sama {self.name}-kun >//<")

re = Student("Re", 18)

print(re.__dict__, "\n")
print(re.incrementAge())

re.sayWaifu()
