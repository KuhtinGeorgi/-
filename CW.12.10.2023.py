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

#2 
