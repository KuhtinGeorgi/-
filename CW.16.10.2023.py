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

#6 Учитывая строку цифр, вы должны заменить любую цифру ниже 5 на "0", а любую цифру 5 и выше - на "1". Верните результирующую строку.
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result

#7

