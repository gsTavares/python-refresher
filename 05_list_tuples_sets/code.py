# lists: uses [ ], with values separated by comma (,)

l = ["Bob", "Rolf", "Anne"]

# tuple: uses ( ), with values separated by comma (,)
# you can't modiy a tuple

t = ("Bob, Rolf", "Anne")

# set: uses { }, with values separated by comma (,)
# you can't put duplicated values in a set

s = {"Bob", "Rolf", "Anne"}

# lists and tuples keeps the order of the elements
# sets does necessarily keeps the order

# accessing values

# subscript notation: can be used in lists and tuples. now allowed for sets
print(l[0])

# modify a list item
l[0] = "Smith"

# adding items at end of a list
l.append("Bob")

# remove elements from a list
l.remove("Bob")

# adding elements to a set
s.add("Smith")
s.add("Smith") # you will not find 2 Smith values in set

print(l)
print(t)
print(s)