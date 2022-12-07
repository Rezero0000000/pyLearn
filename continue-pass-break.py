# pass is like dummy so this is not will execute 

number = 0

while number < 3 :
    number += 1
    print("ini adalah number ke :", number, "\n")

    if number == 2 :
        print("Ketemu angka 2 \n")
        pass

    print("I used arch btw\n")

print("Proses berakhir")

# Continue this will jump to start loop again and "i use arch btw" not execute
print("------- Continue -------")
number = 0

while number < 3 :
    number += 1
    print("ini adalah number ke :", number, "\n")

    if number == 2 :
        print("Ketemu angka 2 \n")
        continue

    print("I used arch btw\n")

print("Proses berakhir")

# Break this is will realy stoped proses
print("------- Break -------")
number = 0

while number < 3 :
    number += 1
    print("ini adalah number ke :", number, "\n")

    if number == 2 :
        print("Ketemu angka 2 \n")
        break

    print("I used arch btw\n")

print("Proses berakhir")

