class Wibu :
    def __init__ (self, name, age, waifu ) :
        self.name = name
        self.age = age
        self.waifu = waifu
        print("Hello World")

    @property
    def sayExpression (self) :
        print(f"{self.waifu} Sayang {self.name}-kun >//<")

re = Wibu("Re", 18, "Rem")
re.sayExpression