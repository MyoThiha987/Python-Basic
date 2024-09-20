# Lambda

squareLambda = lambda num: num * num

def square(num): return num * num

print(square(2))
print(squareLambda(2))

# lambda add num 2
addTwo = lambda num: num + 2
print(addTwo(10))

# lambda sum two num
sum = lambda a, b: a + b
print(sum(5, 2))

###
def funBuilder(x): return lambda num : num + x
addTen = funBuilder(10)
addTwenty = funBuilder(20)
print(addTen(7))
print(addTwenty (7))

# Map
numbers = [3,7 ,12,18,20,21]
square_numbers = lambda num : num * num

print(list(map(square_numbers,numbers)))

# Filter
odd_numbers = filter(lambda num : num % 2 != 0,numbers)
print(list(odd_numbers))

from functools import reduce

total = lambda acc,cur : acc + cur
numbers =[1,2,3,4,5,6,7,8]

print(reduce(total,numbers))


names =['David Gray','Sara Ito','John Jacob Jingleheimerschmidt']
char_count = reduce(lambda acc , crr : acc + len(crr),names,0)
print(char_count)

