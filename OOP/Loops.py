# While Loop

value = 1
while value <=  10:
    print(value)
    if value == 5:
        break
    value += 1

while value <= 10:
    value += 1
    if value == 5:
        continue # skip next line
    print(value)
else:
    print("Current value is now equal to", str(value))

print(" ")

# For Loop
names = ['Dave','Sara','John']
for x in names:
    print(x)

print(" ")

for x in "Mississippi":
    print(x)

print(" ")

for x in names:
    if x == "Sara":
        break
    print(x)
print(" ")
for x in names:
    if x == "Sara":
        continue # skip next line
    print(x)
print(" ")
for x in range(4):
    print(x)
print(" ")
for x in range(2,4):
    print(x)
print(" ")
for x in range(0,100,5):
    print(x)
else :
    print("Glad that\'s over!")

print(" ")
names = ['Dave','Sara','John']
actions = ['Codes','Eats','Sleeps']

for name in names:
    for action in actions:
        print(name + " " + action + ".")
print(" ")
for action in actions:
    for name in names:
        print(  + " " + action + ".")

