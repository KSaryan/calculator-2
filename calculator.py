"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
#importing math functions from external file
from arithmetic2 import *



def my_reduce(math_function, num_list):
    """reduces math calculations
    
    gets calculator input and checks operator to determine what math function to use 
    and does operation with any number of inputs"""

    if math_function == "add":
        total = 0
        for num in num_list:
            total = total + int(num)

    elif math_function == "subtract":
        total = int(num_list[0])
        for i in range(1, len(num_list)):
            total = total - int(num_list[i])
    elif math_function == "multiply":
        total = 1
        for num in num_list:
            total *= int(num)
    elif math_function == "divide":
        total = int(num_list[0])
        for i in range(1, len(num_list)):
            total /= float(num_list[i])
    return "{:.2f}".format(total)

#takes inputs from external file and stores as inputs
inputs = open("inputs.txt")

#reads each line of inputs and separates into list of of math operation and operants
#allows user to quit
#uses my_reduce function
#uses math operation to decide output
#while True:
    #line = raw_input(">>>")
    #line = line.split(" ")

for line in inputs:
    line = line.rstrip()
    #print line
    line = line.split(" ")
    #print line
    if line[0] == "q":
        break
    else:
        try:
            if line[0] == "+":
                print my_reduce("add", line[1:])
            elif line[0] == "-":
                print my_reduce("subtract", line[1:])

            elif line[0] == "*":
                print my_reduce("multiply", line[1:])

            elif line[0] == "/":
                print my_reduce("divide", line[1:])

            elif line[0] == "square":
                if len(line) == 2:
                    print int(line[1]) ** 2
                else:
                    print "Please only input 1 number"
            elif line[0] == "cube":
                if len(line) == 2:
                    print int(line[1])**3
                else:
                    print "Please only input 1 number"
            elif line[0] == "pow":
                if len(line) == 3:
                    print "{:.2f}".format(int(line[1])**int(line[2]))
                else:
                    print "Please only input 2 numbers"
            elif line[0] == "mod":
                if len(line) == 3:
                    print "{:.2f}".format(int(line[1]) % int(line[2]))
                else:
                    print "Please only input 2 numbers"
            else:
                print "not a valid math operator. Please use + - * / mod cube pow or square."
        #checks if input is valid number
        except:
            print "Not a valid number or math operator"

inputs.close()
