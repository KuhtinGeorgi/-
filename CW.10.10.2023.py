#1
def invert(lst):
    a = [num * -1 for num in lst]
    return a
    pass

#2
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#3
def square_sum(number):
    a = 0
    for num in number:
        a += num**2
    return a

#4
def greet():
    return "hello world!"

#5
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2

#6
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False

#7
def greet(name):
    return "Hello, " + name + " how are you doing today?"
    pass

#8
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

#9
def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

#10
def string_to_array(s):  
    return s.split(" ")
