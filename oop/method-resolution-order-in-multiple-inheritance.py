class Kakek :
    def makan (self) :
        print("Kakek makan")    

class Nenek :
    def makan (self) :
        print("Nenek makan")    

class Ayah (Kakek, Nenek) :
    def makan (self) :
        print("Ayah makan")    

class Ibu :
    def makan (self) :
        print("Ibu makan")    
    
class Anak(Ayah) :
    def makan (self) :
        print("Anak makan")    

re = Anak()
help(re)