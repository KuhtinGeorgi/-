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
