# deep copy use for nested list or something like that

users = [ ["Re", "Kazuto", "Schwartz"], ["Rem", "Elaina", "Chitoge"]]
users2 = users.copy()

print(f"users : {users}")
print(f"users2 form users.copy: {users2}\n")

print("users2[0][0] = 'shadow'\n")
users2[0][0] = "shadow"

print(f"users : {users}")
print(f"users2 : {users2}\n")

print("---- using deep copy ---- \n")

from copy import deepcopy

users = [ ["Re", "Kazuto", "Schwartz"], ["Rem", "Elaina", "Chitoge"]]
users3 = deepcopy(users)

print(f"users : {users}")
print(f"users3 form users.copy: {users3}\n")

print("users3[0] = 'shadow'\n")
users3[0][0] = "shadow"

print(f"users : {users}")
print(f"users3 : {users3}\n")