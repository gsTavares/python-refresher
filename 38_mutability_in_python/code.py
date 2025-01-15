a = []
b = a
b.append(1)

print(a, b) # [1] [1]
print(id(a), id(b)) # it will be the same id/reference

a_str = "hello"
b_str = a

print(id(a_str))
print(id(b_str))

a += "world"