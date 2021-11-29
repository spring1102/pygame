#_init_() 函数
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(self.name +" roll over.")
dog1 = Dog("Tom",5)
print(dog1.name)
print(dog1.age)
dog1.sit()
dog1.roll_over()