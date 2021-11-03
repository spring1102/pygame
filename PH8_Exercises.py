#创建类
class enemy:
    def __init__(self,livesLeft,HP):
        #添加属性和方法
        self.lives = livesLeft
        self.health = HP
    def jump(self):
        print("Jump!")
#创建对象
enemy1 = enemy(30,"healthy")
print(enemy1.lives)
print(enemy1.health)
enemy1.jump()