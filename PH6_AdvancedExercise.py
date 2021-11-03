#1.寻找特殊数字，AB为四位数的高两位，CD为低两位,EF为两数之和
#可以设置断点来debug
i = 1000
while i <= 9999:
    AB = int(i/100)
    CD = i%100
    EF = AB + CD
    if EF**2 == i:
        print(i)
    i = i+1
#2.打印特定的菱形图案
while True:
    length = input("Enter the diagonal length:")
    length = float(length)    
    if length <= 0 or length % 2 ==0:
        print("Please enter an odd positive number!")
    else:
        n = int(length)   
        for i in range(-int(n/2),int(n/2)+1):
            print(" "*abs(i),"*"*abs(n-abs(i)*2))
        break