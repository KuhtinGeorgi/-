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
