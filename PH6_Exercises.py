#输出1-10
print("#1")
i = 1 
while i < 11:
  print(i)
  i += 1
print("")
#输出1-10，到4的时候中断
print("#2")
i = 1
while i < 11:
  print(i)
  if i == 4:
    break
  i += 1
print("")
#打印单词中每个字母
print("#3")
for x in "strawberry":
  print(x)
print("")
#打印列表中每个项目
print("#4")
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
for x in fruits:
  print(x)
print("")
#for循环嵌套输出
print("#5")
adj = ["fresh", "big", "tasty"]
vegetables = ["cabbage", "potato", "tomato"]
for x in adj:
  for y in vegetables:
    print(x, y) 
print("")