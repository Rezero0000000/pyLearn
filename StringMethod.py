# Concat
wibu = "Re"
waifu = "Rem"

print(waifu, "sayang " + wibu, ">//<")

# Count string lenght
wibu = "Kazuto Kun"
print("panjang", wibu, ":", len(wibu)) # 10 spasi dihitung

# Check string contain value
value = "r"
status = value in "Schwartz"
print(value, "ada di Schwartz",":", status)

value = "R"
status = value in "Schwartz"
print(value, "ada di Schwartz",":", status)

print("")

# Looping string
print("wk"*5)
print(7*"wk")

print("")

# Indexing
word = "Nodejs is Javascript runtime"
print("index 0 :" + word[0])
print("index 6 :" + word[6])
print("index -1 :" + word[-1])
print("index -2 :" + word[-2])
print("index [0:3] :" + word[0:4])
print("index [3:7] :" + word[3:8])
print("index[0,2,4,6,8,10] :" + word[0:11:2])

print("")

# get smallest item 
print("min item :", min("Schwartz"))
# get maximum item 
print("max item :", max("Schwartz"))

print("")

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah :", str(ascii_code))

data = 117
print("char untuk ASCII 117 adalah :", chr(data))

print("")

word = "bochi the rock"
result = word.count("o")
print("o in", word, "is :", str(result))

print("")

# uppercase
print(word, "=", word.upper())

# Lowercase
word = "WIBU"
print(word, "=", word.lower())

# Check uppercase
status = word.isupper()
print(word, "is Upper :", str(status))

# Check lowercase
word = "wibu"
status = word.islower()
print(word, "is Lower : ", str(status))

"""
    Another method

    # isalpha() <-- check semua huru
    # isalnum() <-- huruf dan angka
    # isdecimal() <-- angka
    # isspace() <-- spasi, tab, newline \ n
    # istitle() <-- semua kata diawali huruf besar

"""
title = "The Journey Of Elaina"
print(title, "is title =", str(title.istitle()))


# Check start and end word
print("")

status = title.startswith("The")
print("start =", str(status))

status = title.endswith("Elaina")
print("End =", str(status))

print("")

# join() & split()
words = ["Rem", "Sayang", "Re-kun >//<"]
print(words)
print(','.join(words))

print("")

word = "ihkamuwiburekunsuamirem"
print(word.split("re"))

















