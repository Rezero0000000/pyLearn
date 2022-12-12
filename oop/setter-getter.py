
class Student :
    def __init__ (self, name, age, waifu) :
        self.name = name
        self.age = age
        self.__waifu = waifu

    @property
    def waifu (self) :
        pass

    @waifu.getter
    def getWaifu (self) :
        return self.__waifu

    @waifu.setter
    def setWaifu (self, value) :
        self.__waifu = value
        print("Waifu Berhasil di update")
    
re = Student("Re", 18, "Elaina")
print(f"Before: {re.getWaifu}")
re.setWaifu = "Rem"
print(f"After: {re.getWaifu}")