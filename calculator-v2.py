def calculate (*args, **kwargs) :
    output = 0

    if kwargs["option"] == "tambah" :
        for i in args :
            output += i
    elif kwargs["option"] == "kali" :
        output = 1
        for i in args :
            output *= i
    else :
        print("Ups salah")

    return output

print(f"Hasil perjumlahan :{calculate(1,2,3,4, option = 'tambah')}")
print(f"Hasil perkalian :{calculate(1,2,3,4, option = 'kali')}")
