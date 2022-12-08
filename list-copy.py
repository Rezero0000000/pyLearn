# Copy list with same addres
users = ["Re", "Ryan", "Kazuto"]
print(f"users : {users}")

wibu = users
print(f"wibu : {wibu}\n")

wibu[2] = "Schwartz"
print(f"users : {users}")
print(f"wibu : {wibu}\n")

# Copy list with diffirent addres
wibu2 = users.copy()
print(f"wibu2 : {wibu2}\n")

wibu2[2] = "Kazuto"
print(f"users : {users}")
print(f"wibu2 : {wibu2}\n")


 