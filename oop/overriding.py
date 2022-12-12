class Siswa : 
    def __init__ (self , nama, umur, kelas):
        self.nama = nama
        self.umur = umur 
        self.kelas = kelas

    def getNama (self) :
        print(f"Nama : {self.nama}")
        
    def getStatus (self) :
        self.getNama() 
        print(f"Umur : {self.umur}")

class Ipa(Siswa) :
    def __init__(self, nama, umur, kelas, mapel) :
        super().__init__(nama, umur, kelas)
        self.mapel = mapel
    
    def getInfo (self) :
        super().getStatus()
        print(f"Kelas : {self.umur}")
        

re = Ipa("Re", 18, "XII Mipa 5", "Matematika")
re.getInfo()