# Dictionaries

band = {
    "vocals": "Plants",
    "guitar": "Page"
}

band2 = dict(vocals="Plants", guitar="Page")
print(band)
print(band2)
print(len(band))

# Access Items
print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List all key/value
print(band.items())

# Verify a key exist
print("guitar" in band)
print("triangle" in band)

# Change Values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove Item
band.pop("bass")
print(band)
band["drums"] = "Bonham"
print(band)
print(band.popitem())  # tuple
print(band)

# Delete and Clear
band["drums"] = "Bonham"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2

# Copy dictionaries
# band2 = band # Create a reference
# print("Bad Copy")
# print(band2)
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good Copy")
print(band)
print(band2)

# create a dict constructor function
band3 = dict(band)
print("Good Copy")
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1 and False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index or position

# Add an element to a set
nums.add(8)
print(nums)

# Add elements from one set to another set
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Merge two sets into one set
one = {1, 2, 3}
two = {4, 5, 6}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)

