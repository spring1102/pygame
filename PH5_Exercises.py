#检查分数是否大于100万
print("#1")
points = input("please input a number:")
points = float(points)
if points > 1000000:
    print("congratulation！you won！！")
else:
    print("sorry,you lost")
print("")
#检查学生成绩
print("#2")
points = input("please input your grade:")
if points == "A":
    print("your grade is greater than 90!")
elif points == "B":
    print("your grade is greater than 80!")
elif points == "C":
    print("your grade is greater than 70!")
elif points == "D":
    print("your grade is greater than 60!")
else :
    print("your grade is less than 60!")
print("")