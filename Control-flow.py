data = int(input("Masukan nilai :\n"))

# if
if (data <= 100) & (data >= 90) :
    print("Congrats")
# else if
elif (data <= 90) & (data >= 80 ) :
    print("Haha not bad")
elif (data <= 80) & (data >= 70) :
    print("Good")
elif data == 0 : 
    print("LOL")
# else
else : 
    print("Sory you lose, let's try again")
