"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic2 import *


# Your code goes here
def my_reduce(math_function, num_list):
    if math_function == "add":
        total = 0
        for num in num_list:
            total = total + int(num)

    elif math_function == "subtract":
        total = int(num_list[0])
        for i in range(1, len(num_list)):
            total = total - int(num_list[i])
    return total


while True:
    guest_input = raw_input(">>>")
    guest_input = guest_input.split(" ")

    try:
        if guest_input[0] == "q":
            break
        elif guest_input[0] == "+":
            print my_reduce("add", guest_input[1:])
        elif guest_input[0] == "-":
            print my_reduce("subtract", guest_input[1:])

        elif guest_input[0] == "*":
            print reduce(multiply, guest_input[1:])

        elif guest_input[0] == "/":
            print reduce(divide, guest_input[1:])

        elif guest_input[0] == "square":
            if len(guest_input) == 2:
                print int(guest_input[1]) ** 2
            else:
                print "Please only input 1 number"
        elif guest_input[0] == "cube":
            if len(guest_input) == 2:
                print int(guest_input[1])**3
            else:
                print "Please only input 1 number"
        elif guest_input[0] == "pow":
            if len(guest_input) == 3:
                print int(guest_input[1])**int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        elif guest_input[0] == "mod":
            if len(guest_input) == 3:
                print int(guest_input[1]) % int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        else:
            print "not a valid math operator. Please use + - * / mod cube pow or square."
    except:
        print "Not a valid number or math operator"
