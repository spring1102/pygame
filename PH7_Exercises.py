#1.用函数打印最喜欢的颜色
print("#1")
def my_function():
  print("My  favorite color is blue.")
my_function()
print("")
#2.接收消息并打印消息的函数
print("#2")
def PrintFunction(fruit):
	print(fruit)
PrintFunction("apple")
print("")
#3.接收数字并相加输出结果
print("#3")
def add(num1, num2):
	print(num1+num2)
add(8,6)
print("")
#4.求圆的面积
print("#4")
radius = int(input("please enter radius ："))
def Erea(r):
    area = 3.14*r
    return area
area = Erea(radius)
print("The area of the circle is" )
print(area)
print("")
#5.计算三角形面积
print("#5")
height = float(input("Please enter the height of the triangle ："))
base = float(input("Please enter the base of the triangle ："))
def EreaTiangle(base,height):
    area = 1/2*base*height
    return area
area = EreaTiangle(base,height)
print("The area of the triangle is" )
print(area)
print("")

