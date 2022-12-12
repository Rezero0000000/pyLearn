class Siswa : 
    def __init__ (self , nama, umur, kelas):
        self.nama = nama
        self.umur = umur 
        self.kelas = kelas
        print("\nHallo Siswa Baru\n")

class Ipa(Siswa) :
    def __init__(self, nama, umur, kelas, mapel) :
        super().__init__(nama, umur, kelas)
        print("Hallo Anak Ipa")
        self.mapel = mapel


re = Ipa("Re", 18, "XII Mipa 5", "Matematika")
print(re.__dict__, "\n")
