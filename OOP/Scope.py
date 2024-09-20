# Scope

name = 'Dave'
count = 1


def greeting(name):
    color = "blue"
    print(color)
    print(name)


# greeting('John')

def another():
    color = "blue"
    global count # Access global variable
    count +=  1

    print(count)
    def greeting(name):
        nonlocal color # Access variable from parent method
        color = "red"
        print(color)
        print(name)
    greeting('Dave')

another()
