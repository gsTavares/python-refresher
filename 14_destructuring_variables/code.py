t = (5, 11)
x, y = t

print(x, y) # 5, 11

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

name, _, profession = people[1] # I want to ignore the age

print(name, profession)

head, *tail = [1, 2, 3, 4, 5]

print(head) # 1
print(tail) # [2, 3, 4, 5]

*first, tail = [1, 2, 3, 4, 5]

print(*first) # 1, 2, 3, 4
print(tail) # 5

