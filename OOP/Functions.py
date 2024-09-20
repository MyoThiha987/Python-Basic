# Functions

def hello_world():
    print('Hello World!')


hello_world()


def sum(num1, num2=3):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


total = sum(2, 3)
print(total)


def multiple_items(*args):  # * means Multiple Items
    print(args)
    print(type(args))


multiple_items({"hello": "world"})  # tuple


def mult_named_items(**kwargs):  
    print(kwargs)
    print(type(kwargs))

mult_named_items(first="Dave",last="John")
