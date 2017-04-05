"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    guest_input = raw_input(">>>")
    guest_input = guest_input.split(" ")
    if guest_input[0] == "q":
        break
    elif guest_input[0] == "+":
        print int(guest_input[1]) + int(guest_input[2])
    elif guest_input[0] == "-":
        print int(guest_input[1]) - int(guest_input[2])
    elif guest_input[0] == "*":
        print int(guest_input[1]) * int(guest_input[2])
    elif guest_input[0] == "/":
        print float(guest_input[1]) / int(guest_input[2])
    elif guest_input[0] == "square":
        print int(guest_input[1]) ** 2
    elif guest_input[0] == "cube":
        print int(guest_input[1])**3
    elif guest_input[0] == "pow":
        print int(guest_input[1])**int(guest_input[2])
    elif guest_input[0] == "mod":
        print int(guest_input[1]) % int(guest_input[2])
    else:
        print "not a valid input"
