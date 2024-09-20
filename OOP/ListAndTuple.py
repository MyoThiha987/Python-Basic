# List

users = ['Dave', 'John', 'Sara']
data = ['Dave', 42, True]
emptyList = []
print("Dave" in emptyList)
print(users[0])
print(users[-1])
print(users[-2])
print(users.index('Dave'))
print(users[1:])
print(users[-3: -1])
print(len(users))
print(len(data))
users.append('Elsa')
users += 'Jason'
users += ['Jason', 'Hello']
users.extend(['Robert', 'Jimmy'])
print("Blah,Blah", users[0:2])
# users.extend(data)
users.insert(0, "Johny")
users[2:2] = ['Eddie', 'Alex']
users[1:3] = ['Robert', 'JPJ']
users.remove('J')
print(users)
del users[0]
print(users)

data.clear()
print(data)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
nums.sort(reverse=True)

print(sorted(nums))
print(" ")

num_copy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(num_copy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

my_tuple = tuple(('Dave', 43, True))
another_tuple = (1, 4, 2, 8, 6, 4, 4)
print(my_tuple)
print(another_tuple)
print(type(my_tuple))
print(type(another_tuple))

newlist = list(my_tuple)
newlist.append('Neil')
newTuple = tuple(newlist)
print(newTuple)
print(newlist)

# * more than one value
(one, two, *hey) = another_tuple
print(f"{one}\n{two}\n{hey}")
print(another_tuple.count(4))


