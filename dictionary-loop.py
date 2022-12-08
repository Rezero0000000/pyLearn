players  = {
    "knight" : "Schwartz",
    "thief" : "Kazuto",
    "mage" : "chisato",
    "assasin" : "re"
}

# Loop fisrt try (for key return)

for role in players :
    print(role)

# Operator to get item / iterables

# Normal

keys = players.keys()
print(f"\n{keys}\n") 

# By key
for key in players.keys() :
    print(f"Role : {key} | Player : {players.get(key)}")

print("")

# By value
for value in players.values() :
    print(f"Player Name : {value}")

print("")

# By item 
for item in players.items() :
    print(f"Player : {item}")

print("")

# Get the key and value 
for role,player in players.items() :
    print(f"Role : {key} | Player : {player}")
    