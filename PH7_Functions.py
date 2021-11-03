#递归函数
def factorial(x):
       if x == 1:
           return 1
       else:
            return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))
