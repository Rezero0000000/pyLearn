user = {
    "Name" : "Re",
    "Age" : 17,
    "Waifu" : "rem"
}
print(f"\nData : {user}")

# Count dictionary length ("Becaus i named the variable like constant so it write on uppercase letter")
LENDICT = len(user)
print(f"\nData length: {LENDICT}")

# Check dictionary contains key or no
KEY = "Waifu"
status = KEY in user
print(f"user contain {KEY} : {status}\n")

# Access value with get method
print(user["Name"])
print(user.get("Name"))
print(user.get("HP", "Data key tidak ditemukan :(\n"))

# Update data with update
print(f"user['Name'] : {user['Name']}")
user["Name"] = "Schwartz"
print(f"user['Name'] : {user['Name']}")
user.update({"Name":"Kazuto"})
user.update({"HP":100})
print(f"\nData : {user}")

# So if in the dictionary not found key when u updated data so it automate insert into the dictionary 

# Delete data
del user["HP"]
print(f"\nData : {user}")




