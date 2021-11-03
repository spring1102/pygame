#1.a 输入摄氏度，输出华氏温度

#获取输入的数值
Celsius = input("Please enter Celsius：")
#转化为float类型
FloatCelsius = float(Celsius)
#进行运算
Fahrenheit = 9/5*2*FloatCelsius + 32
#输出结果
print("The temperature in Fahrenheit is:" + '%.2f' % Fahrenheit)

#1.b 华氏温度转化为开氏温度
Kelvin = (Fahrenheit + 456.78) * 5 / 9
print("The temperature in Kelvin is:" + '%.2f' % Kelvin)
