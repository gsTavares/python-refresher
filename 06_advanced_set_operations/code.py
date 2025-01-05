friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# remove all elements from first set that exists on the second set
local_friends = friends.difference(abroad)

# union of two sets
all_friends = local_friends.union(abroad)

print(local_friends)
print(f"Union of local friends and abroad friends: {all_friends}")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# set intersection: compares two sets and return a new set with the elements that are in both of them
both = art.intersection(science)

print(both)