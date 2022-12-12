class Siswa : 
    def __init__ (self , nama, umur, kelas):
        self.nama = nama
        self.umur = umur 
        self.kelas = kelas
        print("Hallo Siswa Baru")

class Ipa(Siswa) :
    pass


re = Ipa("Re", 18, "XII Mipa 5")
print(re.__dict__)
