# String Format

person = "Dave"
coins = 3

print("\n" + person + " "+"has " + str(coins) + " " + "coin left")

message = "\n%s has %s coins left" % (person,coins)
print(message)
print(" ")
message = "\n{} has {} coins left".format(person,coins)
print(message)
print(" ")
message = "\n{0} has {1} coins left".format(person,coins)
print(message)
print(" ")
message = "\n{person} has {coins} coins left".format(person =person,coins =coins)
print(message)

player = {
    "person" : "Dave",
    "coins" : "3"
}
message = "\n{person} has {coins} coins left".format(**player)
print(message)

# FString
message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person} has {2*5} coins left"
print(message)

message = f"\n{player['person' ] } has {2*5} coins left"
print(message)

# You can pass formatting options
num = 10
print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num/4.52:.2%}")


