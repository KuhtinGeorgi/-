def invert(lst):
    a = [num * -1 for num in lst]
    return a
    pass

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
