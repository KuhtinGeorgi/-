#1 Светофор
def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    elif current == 'red':
        return 'green'

#2 Sykpzdc.....
def repeat_str(repeat, string):
    return repeat * string

#3 Перемножить все числа в массиве
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
  
