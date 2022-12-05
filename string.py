example = "Hello World"
print(example)
print(type(example))

# 1. Cara Membuat string
'''
    1. Dengan single quote '...'
    2. Dengan double quote "..."
'''

data = 'single quote'
print(data)

print("")

data = "double quote"
print(data)

# 2. condition
print('"IH WIBU"')
print("'Halo Apa kabar ?")

# 3. Menggunakan tanda \
'''
    Salah :
            print('aku suka YO'ASOBI')
    Benar :
            print('aku suka YO\'SOBI)
'''
# example
print('the sky look beautiful is\'t it?')

# Backslash
print("C:\\user\\re")

# Tab [\t]
print("aku\tdan\tdia, berjauhan")

# Backspace [\b]
print("aku \bdan \bdia, deketan")

# Newline [\n, \r, \r\n]
print("")
print("Baris pertama. \nbaris kedua.") # LF -> line feed -> unix, macos, kinux
print("__________________________________") 
print("Baris pertama. \rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("__________________________________") 
print("Baris pertama. \r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

# 4. String literal (Raw)

# Note
print('C:\new folder') # Akan Salah pathnya

# Raw string
print(r'C:\new folder')

# Multiline string / Literal string
print("""
    Name : Re
    Age : 18
""")

# Multiline literal string with Raw
print(r'''
    Nama : Re
    Age : 18
    Sekolah : SMA\new normal
    website : rekun.vercel.app/Home
''')

# String format

print("")

waifu = "Rem"
wibu = "Re"

print(f"{waifu} Sayang {wibu}-kun >//<")

ini = 18
print(f"Ini kontent {ini:+d}")
 





