# boolean comparison
print(5 == 5) # True
print(5 > 5) # False
print(10 != 10) # False

# comparison: ==, !=, <, >, >=, <=
# some comparisons don't work on dome data types

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad) # True
print(friends is abroad) # False, because the two lists have different memory addresses