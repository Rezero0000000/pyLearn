# Simple function

def hello() :
    print("Hello World\n")

hello()

# Functionn with parameter
def sayHello (name = "User") :
    print(f"Ohayo {name}-kun~")

sayHello("Re")

# Function with default parameter
def sayHello (name = "User") :
    print(f"Ohayo {name}-kun~")

sayHello()

def calculate(num1, num2) :
    total = num1 + num2
    return total

print(calculate(2,3), "\n")

def listPlayer (players) :
    index = 0   
    for player in players :
        index += 1
        print(f"[{index}]. {player}")

players = ["Re", "Ryan", "Schwartz"]
listPlayer(players)

print("")

# Multiple return
def calculateOperation(num1, num2) :
    perjumlahan = num1 + num2
    pengurangan = num1 - num2
    perkalian = num1 * num2
    pembagian = num1 / num2

    return perjumlahan, pengurangan, perkalian, pembagian
a, b, c, d = calculateOperation(10, 2)
print(f"Perjumlahan = {a}")
print(f"pengurangan = {b}")
print(f"Perkalian = {c}")
print(f"Pembagian = {int(d)}\n")

# Type Hinting
def calculateNumber(num1 : int, num2 : int) -> int :
    return num1 + num2

print(calculateNumber(2,3), "\n")

# args
def printPlayers (*players) :
    index = 0
    for player in players:
        index += 1
        print(f"[{index}]. {player}")

printPlayers("Re","Ryan","Schwartz \n")

# Kwargs (For dictionary)
def printMage (**kwargs) :
    print(kwargs, "\n")
    print(kwargs["Name"])
    print(kwargs["Age"])

printMage(Name="Re",Age=17)



