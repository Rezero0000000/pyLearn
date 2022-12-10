name = "Re"

def changeName (newName:str) :
    name = newName

changeName("Schwartz")
print(name)

def changeName_v2(newName:str) :
    global name
    name = newName

changeName_v2("Schwartz")
print(name)
