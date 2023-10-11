def invert(lst):
    a = [num * -1 for num in lst]
    return a
    pass

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def square_sum(number):
    a = 0
    for num in number:
        a += num**2
    return a

def greet():
    return "hello world!"

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False

def greet(name):
    return "Hello, " + name + " how are you doing today?"
    pass
