waifus = ["rem", "chitoge", "elaina", "kurumi", "itsuki"]
print("data waifus :",waifus, "\n")

# Indexing
print(f"waifus[0] : {waifus[0]}")
print(f"waifus[1] : {waifus[1]}")
print(f"waifus-10] : {waifus[-1]}")
print(f"waifus[21] : {waifus[-2]}\n")

# Count list length
print("waifus length :", len(waifus), "\n") 

# Insert item by index
print(f"before : {waifus}")
waifus.insert(2, "onodera")
print(f"after : {waifus}\n")

# Insert item in last list
print(f"before : {waifus}")
waifus.append("Ayano")
print(f"after : {waifus}\n")

# Insert list with list
fruits = ["apel", "grape"]
print("data fruits :",fruits, "\n")

fruits2 = ["watermelon", "orange"]
fruits.extend(fruits2)
print("fruits :",fruits, "\n")

# Remove item
fruits.remove("grape")
print("data fruits :",fruits, "\n")

# Remove last item
fruits.pop()
print("data fruits :",fruits, "\n")

# Count same item in list
numbers = [1,2,3,5,1,2,3,5,9,5,3,1,7]
print("data numbers :",numbers, "\n")

print(f"angka 1 : {numbers.count(1)}")
print(f"angka 5 : {numbers.count(5)}\n")

# Get list index position
print(f"Data waifu : {waifus}")
print(f"waifus.index('rem') : {waifus.index('rem')}")
print(f"waifus.index('elaina') : {waifus.index('elaina')}\n")


