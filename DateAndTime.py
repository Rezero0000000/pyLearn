import datetime as time

today = time.date.today()

print(f"Today is {today:%A}")


print("Silahkan masukan :")
tanggal = int(input("Tanggal "))
bulan = int(input("Bulan "))
tahun = int(input("Tahun "))

inputTime = time.date(tahun, bulan, tanggal)
print(f"anda lahir hari {inputTime:%A}")

umurHariIni = time.date.today() - inputTime
umurTahun = umurHariIni / 365
print(f"umur anda adalah : {umurTahun}")
