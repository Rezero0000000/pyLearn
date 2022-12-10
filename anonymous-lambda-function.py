# Simple functiom
def hello () : 
    print("Hello World")

# Lambda
sayHello = lambda name : print(f"Hello {name}")
sayHello("Re")

# Implementation
users = ["Re", "Kazuto", "Schwartz"]
users.sort(key=len)

print("Data Sort :",users, "\n")

# Filtering
numbers = [8,10,25,1,5,32,7,29,5]
print(f"Data filter : {list(filter(lambda x:x<9, numbers))}")

genap = list(filter(lambda x:(x%2==1), numbers))
print(f"Data ganjil : {genap}")
print(f"Data filter : {list(filter(lambda x:(x%2==0), numbers))}")

# Anonymous function
# Currying <-- Haksel Curry

def pangkat(n) :
    return lambda angka:angka**n

print(pangkat(2)(2))


