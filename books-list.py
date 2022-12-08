books = []

while True :
    print("Masukan data buku")
    judul = input("Judul buku : ")
    penulis = input("Penulis buku : ")

    newBook = [judul, penulis]
    books.append(newBook)

    print("\n========== Boooks =========")

    for i,book in enumerate(books) :
        i += 1
        print(f"[{i}]. {book[0]} | {book[1]}")

    print("\n")
    status = input("Apa anda ingin memasukan daftar lagi ? (y/n)")
    if status == "n" :
        break
    
print("Terimakasih sudah berkunjung ^^")

