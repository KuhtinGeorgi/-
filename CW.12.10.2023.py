#1 Ваша задача — создать функцию, которая может принимать в качестве аргумента любое неотрицательное целое число и возвращать его с цифрами в порядке убывания.
def descending_order(num):
    counter = 0
    arr = list(str(num))
    for i in arr:
        arr[counter] = int(i)
        counter += 1
    arr.sort()
    arr = list(reversed(arr))
    ans = ''
    for i in arr:
        ans += str(i)
    return int(ans)

#2 Изограмма – это слово, в котором нет повторяющихся букв, как последовательных, так и непоследовательных. 
Реализуйте функцию, которая определяет, является ли строка, содержащая только буквы, изограммой.
def is_isogram(string):
    string = string.lower()
    arr = list(string)
    for j in range(0, len(arr), 1):
        sym = 0
        for i in arr:
            if i == arr[j]:
                sym += 1
                if sym == 2:
                    return False
    return True

#3 Часы показывают hчасы, mминуты и sсекунды после полуночи.
Ваша задача — написать функцию, возвращающую время с полуночи в миллисекундах.
def past(h, m, s):
    return s * 1000 + m * 60000 + h * 3600000

#4 Завершите решение так, чтобы оно возвращало true, если первый переданный аргумент (строка) заканчивается вторым аргументом (также строкой).
def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False

#5 Создайте функцию, которая отвечает на вопрос «Вы играете на банджо?».
Если ваше имя начинается с буквы «R» или строчной «r», вы играете на банджо!
def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"

#6 Проверьте, содержит ли строка одинаковое количество символов «x» и «o». 
def xo(s):
    s = s.lower()
    
    arr = list(s)
    xCount = 0
    oCount = 0
    for i in arr:
        if i == 'o':
            oCount += 1
        elif i == 'x':
            xCount += 1
    if xCount == oCount:
        return True
    else:
        return False

#7 Просто, учитывая строку слов, верните длину самого короткого слова (слов).
def find_short(s):
    arr = s.split(' ')
    l = arr[0]
    for i in arr:
        if len(l) > len(i):
            l = i
    return len(l)
