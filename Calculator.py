print("\n")
print("-"*30)
print("    KALKULATOR SEDERHANA")
print("-"*30)

opsi = int(input("""
Masukan operasi :\n
[1]. Perjumlahan
[2]. Pengurangan
[3]. Perkalian
[4]. Pembagian
"""))



if opsi == 1 :
    number1 = int(input("Masukan angka pertama \n"))
    number2 = int(input("Masukan angka kedua \n"))
    print(f"\n{number1} + {number2} = {number1 + number2}\n")
elif opsi == 2 :
    number1 = int(input("Masukan angka pertama \n"))
    number2 = int(input("Masukan angka kedua \n"))
    print(f"\n{number1} - {number2} = {number1 - number2}\n")
elif opsi == 3 :
    number1 = int(input("Masukan angka pertama \n"))
    number2 = int(input("Masukan angka kedua \n"))
    print(f"\n{number1} * {number2} = {number1 * number2}\n")
elif opsi == 4 :
    number1 = int(input("Masukan angka pertama \n"))
    number2 = int(input("Masukan angka kedua \n"))
    print(f"\n{number1} / {number2} = {number1 / number2}\n")
else :
    print("\nInputan Salah\n ")

print("Terimakasi sudah berkunjung ^^")