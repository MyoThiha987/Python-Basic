import math

# Python Basics
greeting = 'Hello World!'
print(greeting)

line1 = "******************"
line2 = "*                *"
line3 = "*    Welcome     *"

print('')
print(line1)
print(line2)
print(line3)
print(line2)
print(line1)

# Operators
name = "Mg Mg"
print("Name :", name)
sum = 4 + 2
print("Plus Operator :", sum)
minus = 3 - 1
print("Minus Operator :", minus)
multiply = 4 * 2
print("Multiply Operator :", multiply)
divide = 4 / 2
print("Divide Operator :", round(divide))
floor_division = 4 // 2
print("Floor Division :", floor_division)
remainder = 42 % 4
print("Remainder :", remainder)
times = 2 ** 3
print("Times :", times)
meaning = 8
meaning += 1
meaning -= 1
meaning *= 10
meaning /= 10
print(round(meaning))
print(meaning)
meaning = round(meaning)
print(meaning)
name = "Mg Mg" + " " + "Zaw"
print(name)
equal = 42 == 41
print("Equal :", equal)
not_equal = 42 != 42
print("Not Equal :", not_equal)
greater_than = 10 > 3
print("Greater than :", greater_than)
less_than = 20 < 3
print("Less than :", less_than)
greater_than_equal = 10 >= 3
print("Greater than equal :", greater_than_equal)
less_than_equal = 20 <= 3
print("Less than equal :", less_than_equal)
x = True
y = False
z = True
not_x = not x
print("Not X :", not_x)
not_y = not y
print("Not Y :", not_y)
x_and_y = x and y
print("X and Y :", x_and_y)
y_and_x = y and x
print("Y and x :", y_and_x)
x_or_y = x or y
print("X or Y :", x_or_y)
x_and_z = x and z
print("X and Z :", x_and_z)
z_and_y = z and y
print("Z and Y :", z_and_y)
y_or_z = y or z
print("Y or Z :", y_or_z)

if meaning > 8:
    print("Right On!")
else:
    print("Not Today! ")

# Ternary Operator
print("Right On!") if meaning > 10 else print("Not Today! ")

# Data Types
# Literal Assignments
first = "Dave"
second = "Gray"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor Functions

pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + second
print(fullname)
fullname += "!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)
statement = "I like rock music from the " + decade + "s"
print(statement)

# Multiple Lines
multiline = '''
Hey,how are you?

I was just checking in.

                        All good?
'''
print(multiline)

# Escaping Special Characters
sentence = 'I\'m back at work\tHey\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
print(len(multiline))
multiline += "                   "
multiline = "                    " + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print(" ")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(20, ".") + "$1".rjust(4))  # Left Side Justify string
print("Muffin".ljust(20, ".") + "$2".rjust(4))
print("Cheesecake".ljust(20, ".") + "$4 ".rjust(4))
print(" ")

# String index
print(first[1])
print(first[-1])
print(first[1:-1])  # Not include last index
print(first[1:])  # include last index

# Returning boolean
print(first.startswith("D"))
print(first.endswith("D"))

# Boolean Data Type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(x, bool))

# Numeric Data type

# Integer type
price = 20
best_price = int(100)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# Complex Type
comp_value = 3 + 2j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)

print(math.sqrt(64))
print(math.ceil(gpa))  # take 4 for 3.28
print(math.floor(gpa))  # take 3 for 3

# Casting a string to number
zip_code = "10001"
zip_value = int(zip_code)
print(type(zip_value))

user_name = input("Enter your name : \n")
password = input("Enter your password : \n")
print(f"Your name is : {user_name} and password is {password}")

# Error if you attempt to cast incorrect data
# zip_value = int("Zeeer")
# print(zip_value)

# User Input
import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_win = 0
    python_win = 0

    def play_rps():
        nonlocal player_win
        nonlocal python_win

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print(RPS(2))
        print(RPS.ROCK)
        print(RPS['ROCK'])
        print(RPS.ROCK.value)

        print(" ")
        player_choice = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

        if player_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2 or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        print(" ")

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"\nPython chose {str(RPS(computer)).replace('RPS.', '').title()}. ")
        print(" ")

        def decide_winner(player, computer):
            nonlocal player_win
            nonlocal python_win

            if player == 1 and computer == 3:
                player_win += 1
                return "🎉You win!"
            elif player == 2 and computer == 1:
                player_win += 1
                return "🎉You win!"
            elif player == 3 and computer == 2:
                player_win += 1
                return "🎉You win"
            elif player == computer:
                return "😮Tie game!"
            else:
                python_win += 1
                return "🐍Python win!"
            print("\nPlay again?\n")

        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1

        print(f"\nGame Count : {str(game_count)}", )
        print(f"\nPlayer win : {str(player_win)}")
        print(f"\nPython win : {str(python_win)}")

        while True:
            play_again = input("Y for Yes or\n Q  for Quit\n\n ")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            print("Bye!")
            sys.exit()
    return play_rps


rock_paper_scissor = rps()

if __name__ == "__main__" :
    rock_paper_scissor()
