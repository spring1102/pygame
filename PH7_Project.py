#使用函数返回列表数字的和
def sumOfList(number):
    i = 0
    sum = 0
    while i < len(number):
        sum = sum + number[i]
        i = i + 1
    return sum
#list可以自定义，或者输入
list = [5, 6, 7, 8, 9]
sum = sumOfList(list)
print(sum)

