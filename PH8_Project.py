#创建类
class enemy:
    def __init__(self,livesLeft,HP,s,name):
        #添加属性和方法
        self.lives = livesLeft
        self.health = HP
        self.score = s
        self.name = name
    def jumping(self):
        print("Jump!")
    def moving(self):
        print(self.name + " is moving")
    def healing(self):
        print(self.name + " is healing")
    def attacking(self):
        print(self.name + " is attacking")
#创建对象
#显示所有属性，运行每个方法
enemy1 = enemy(30,"healthy",200,"Tom")
print(enemy1.lives)
print(enemy1.health)
print(enemy1.score)
print(enemy1.name)
enemy1.jumping()
enemy1.moving()
enemy1.healing()
enemy1.attacking()