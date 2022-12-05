a = True
b = False

print("_____ [NOT] _____")
print(a, "=", a)
print("not", a, "=", not a )

print("")
print("_____ [OR] _____")
print(a, "OR", b, "=", a or b)
print(b, "OR", a, "=", b or a)
print(a, "OR", a, "=", a or a)
print(b, "OR", b, "=", b or b)

print("")
print("_____ [AND] _____")
print(a, "AND", b, "=", a and b)
print(b, "AND", a, "=", b and a)
print(a, "AND", a, "=", a and a)
print(b, "AND", b, "=", b and b)

print("")
print("_____ [XOR ^] _____")
print(a, "OR ^", b, "=", a ^ b)
print(b, "OR ^", a, "=", b ^ a)
print(a, "OR ^", a, "=", a ^ a)
print(b, "OR ^", b, "=", b ^ b)

# Jka nilai sama false kalau beda true :v
