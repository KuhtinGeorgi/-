#1 В этом небольшом задании вам дается строка чисел, разделенных пробелами, и вы должны вернуть наибольшее и наименьшее число.
def high_and_low(numbers):
    numbers = numbers.split(' ')
    j = 0
    for i in numbers:
        numbers[j] = int(i)
        j += 1
    max1 = str(max(numbers))
    min1 = str(min(numbers))
    return max1 + ' ' +  min1
  
  #2 Создайте функцию, которая возвращает массив целых чисел от n до 1, где n>0.
  def reverse_seq(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return list(reversed(arr))

#3 Завершите функцию, которая принимает строковый параметр и меняет местами каждое слово в строке. 
#Все пробелы в строке должны быть сохранены.
def reverse_words(text):
    text = text.split(' ')
    ans = ''
    for i in text:
        ans += i[::-1] + ' '  
    return ans.strip()
#4 ОДИН ГРЁБАННЫЙ ЧАС Я ЭТО ДЕЛАЛ.
#Есть ли у числа квадратный корень без дробной части.
def is_square(n):
    if n < 0:
        return False
    elif n ** 0.5 % 1 == 0:
        return True
    else:
        return False

#5 Банкоматы допускают использование 4- или 6-значных PIN-кодов, а PIN-коды не могут содержать ничего, кроме ровно 4 или ровно 6 цифр.
def validate_pin(pin):
    if pin.isdigit() == True:
        if len(pin) == 4:
            return True
        elif len(pin) == 6:
            return True
        else:
            return False
    else:
        return False

#6 Удаляет наименьшее число из массива
def remove_smallest(numbers):
    if len(numbers) != 0:
        numbers.pop(numbers.index(min(numbers)))
        return numbers
    else:
        return []

#7 Камеь Ножницы Бумага
def rps(p1, p2):
    rsp = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if rsp[p1] == p2:
        return "Player 1 won!"
    elif rsp[p2] == p1:
        return "Player 2 won!"
    else:
        return "Draw!"

#8 Возвращает массив, где первый элемент — это количество положительных чисел, а второй элемент — сумма отрицательных чисел. 
# 0 не является ни положительным, ни отрицательным.
def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    lenP = 0
    sumN = 0
    for i in arr:
        if (i > 0):
            lenP += 1
        else:
            sumN += i
    return [lenP, sumN]

#9 Строку в верхний регистр
def make_upper_case(s):
    return s.upper()

#10 Удалить ! из строки.
def remove_exclamation_marks(s):
    return s.replace("!", "")
