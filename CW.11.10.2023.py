#1 строку в число
def string_to_number(s):
    return int(s)
    pass
    
#2 противоположность числа
def opposite(number):
    return number * -1

#3 Суть этой ката заключается в умножении заданного числа на восемь, если оно четное, и на девять в противном случае.
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

#4 Напишите функцию, которая принимает массив чисел и возвращает сумму чисел. Числа могут быть отрицательными или нецелыми. Если массив не содержит чисел, вам следует вернуть 0.
def sum_array(a):
    if sum(a) == 0:
        return 0
    else:
        return sum(a)

#5 Кодируйте как можно быстрее! Вам нужно удвоить целое число и вернуть его.
def double_integer(i):
    return i * 2

#6 Реализуйте функцию, которая преобразует данное логическое значение в его строковое представление.
def boolean_to_string(b):
    return str(b)

#7 Ваши одноклассники попросили вас скопировать для них кое-какие документы. Вы знаете, что одноклассников n, а в документах m страниц.
def paperwork(n, m):
    if n <= 0:
        return 0
    elif m <= 0:
        return 0 
    else:
        return n * m


