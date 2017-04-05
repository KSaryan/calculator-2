"""Math functions for calculator."""


def add(num_list):
    """Return the sum of the two input integers."""
    total = 0
    for num in num_list:
        total += num
    return total


def subtract(num_list):
    """Return the second number subtracted from the first."""
    total = num_list[0]
    for i in range (1, len(num_list)):
        total -= num_list[i]
    return total


def multiply(num_list):
    """Multiply the two inputs together."""
    total = 1
    for num in num_list:
        total *= num
    return total


def divide(num_list):
    """Divide the first input by the second, returning a floating point."""
    total = float(num_list[0])
    for i in range(1, len(num_list)):
        total /= num_list[i]
    return total


    # Need to turn at least one argument to float for division to
    # not be integer division



def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
