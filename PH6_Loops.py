# while loop
i = 1 
while i < 6:
  print(i)
  i += 1
# using break 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# for loop in list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#for loop in Strings
for x in "banana":
  print(x)

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
