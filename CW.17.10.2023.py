#1 Напишите программу, в которой Алекс может ввести (n), сколько раз вращается обруч, и она вернет ему ободряющее сообщение :)
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"

#2 вернуть инициалы 
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]  

#3 достаточно ли места
def enough(cap, on, wait):
    return max(0, wait - (cap - on))

#4 a+b перевод в двоичную
def add_binary(a,b):
    sum = a + b
    return bin(sum)[2:]

#5 Если указано число от 0 до 9, верните его прописью.
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]

#6 Возможен ли треугольник (7лвл)
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

#7 Светофор Mk2
def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}[current]

#8
