#1 Умножить числа в массиве на 2
def maps(a):
    arr = []
    for i in a:
        arr.append(i * 2)
    return arr

#2 Вычисление объёма кубоида
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#3 Ывывваваавава((((
def get_sum(a,b):
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma

#4 Минимальное и максимальное число в массиве
def min_max(lst):
    return [min(lst), max(lst)]

#4 Удалить первый и последний элемент строки
def remove_char(s):
    return s[1: -1]

#5 Пирамида
def tower_builder(n_floors):
    piramida = []
    for i in range(1, n_floors + 1):
        piramida.append(' ' * (n_floors - i) + '*' * (2 * i-1))
    return piramida

#6 ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

#6 Учитывая строку цифр, вы должны заменить любую цифру ниже 5 на "0", а любую цифру 5 и выше - на "1". Верните результирующую строку.
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

#7 На этот раз никакой истории, никакой теории. Приведенные ниже примеры показывают, как написать функцию accum:
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]

#8 Удалить каждый второй элемент.
def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r

#9 В этом kata вы создадите функцию, которая принимает список неотрицательных целых чисел и строк и возвращает новый список с отфильтрованными строками.
def filter_list(l):
    result =[]
    for x in l:
        if type(x) != str:
            result.append(x)
    return result

#10 Возраст
def get_age(age):
    return int(age[0])


