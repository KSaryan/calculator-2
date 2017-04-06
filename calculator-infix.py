"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    guest_input = raw_input(">>>")
    guest_input = guest_input.split(" ")

    try:
        if guest_input[0] == "q":
            break
        elif guest_input[1] == "+":
            if len(guest_input) == 3:
                print int(guest_input[0]) + int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        elif guest_input[1] == "-":
            if len(guest_input) == 3:
                print int(guest_input[0]) - int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        elif guest_input[1] == "*":
            if len(guest_input) == 3:
                print int(guest_input[0]) * int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        elif guest_input[1] == "/":
            if len(guest_input) == 3:
                print float(guest_input[0]) / int(guest_input[2])
            else:
                print "Please only input 2 numbers"
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
        elif guest_input[1] == "**":
            if len(guest_input) == 3:
                print int(guest_input[0])**int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        elif guest_input[1] == "%":
            if len(guest_input) == 3:
                print int(guest_input[0]) % int(guest_input[2])
            else:
                print "Please only input 2 numbers"
        else:
            print "not a valid math operator. Please use + - * / mod cube pow or square."
    except:
        print "Not a valid number or math operator"
