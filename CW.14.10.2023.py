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
  
#4 вернуть наименьшее число в массиве
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

#5 Вычислите сумму чисел в n-й строке этого треугольника (начиная с индекса 1), например: (Ввод --> Вывод)
def row_sum_odd_numbers(n):
    return n * n * n

#6
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

#7 Напишите функцию bmi, которая вычисляет индекс массы тела (bmi = вес / рост2).
def bmi(weight, height):
    BMI = weight / height ** 2
    if BMI <= 18.5:
        return "Underweight"
    elif BMI <= 25.0:
        return "Normal"
    elif BMI <= 30.0:
        return "Overweight"
    else:
        return "Obese"

#8 Узнать квартал месяца
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    elif month <= 12:
        return 4

#9 Напишите функцию, которая берет массив слов, объединяет их в предложение и возвращает предложение.
def smash(words):
    return ' '.join(words) + '' 

#10 Ъуь
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False
