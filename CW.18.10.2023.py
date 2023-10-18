#1 Удалить гласные
def disemvowel(string_):
    remove = 'AaEeIiOoUu'

    for i in remove:
        string_ = string_.replace(i, "")
    return string_

#2 найти символ, который встречается нечётное кол-во раз
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

#3 Найти число гласных (коекаких)
def get_count(sentence):
    sum = 0
    for i in sentence:
        if i == 'a' or i == 'e' or i == 'i' or i == 'u' or i == 'o':  
            sum += 1
    return sum

#4 Если имя = 4 буквы - друг.
def friend(x):
    friends = []
    for word in x:
        if len(word) == 4:
            friends.append(word)
    return friends

#5 Инверсия регистра
def to_alternating_case(string):
    return string.swapcase()

#6 перевернуть массив без спец функций
def reverse(seq): 
    for i in range(len(seq)>>1):
        seq[i],seq[-i-1] = seq[-i-1],seq[i]

#7 Ывывывывыв
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#8 Принтер и ошибки.
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)

#9  Реализуйте функцию, принимающую n и d в качестве параметров и возвращающую это значение.
def nb_dig(n, d):
    result = 1 if d == 0 else 0
    for k in range(1, n + 1):
        x = k * k
        while x:
            if x % 10 == d:
                result += 1
            x //= 10
    return result

#10 Цифра 5 без цифры 5
def unusual_five():
    five = ['l', 'o', 'l', 'o', 'l']
    return len(five)
