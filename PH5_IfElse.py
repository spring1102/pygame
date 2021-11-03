#just if
age = 12
if age < 7:
	print("It is recommended you watch G rated movies!")
if age < 13:
	print("You can watch PG rated movies!")
if age < 17:
	print("You can watch PG-13 rated movies!")
if age > 17:
	print("You can watch R rated movies!")
print()
#if and elif and else
age = 12
if age < 7:
	print("It is recommended you watch G rated movies!")
elif age < 13:
	print("You can watch PG rated movies!")
elif age < 17:
	print("You can watch PG-13 rated movies!")
else:
	print("You can watch R rated movies!")
print()


#other data types
name = "hellen"
if name == "hellen": #1.checking strings
	print("Hello Madam!")

surname = "Mr."#2.
if surname == "Mr.":
	print ("Hello Sir")
elif surname == "Mrs.":
	print("Hello Madam!")
else:
	print("Hello there!")


if True == True: #3.checks Boolean types
	print("TRUE")
elif False == False:
	print("FALSE")

if 4.5 == 6.5: #4.checks floating point numbers
	print("never gonna work")
else:
	print("Hello there")
