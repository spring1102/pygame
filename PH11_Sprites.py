import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()


pic = pygame.image.load("pictures/plane.png") 
#Player类继承Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
#按键移动图画
def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

#实例化的player
player = Player()
# 主窗口宽高
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#用Boolean进入或退出循环
running = True
while running:
    screen.fill((0, 220, 255))
    surf = pygame.Surface((50, 50))
    surf.fill((255, 0, 0))
    rect = surf.get_rect()
    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))   
    
    for event in pygame.event.get():        
        #键盘：是否按了键       
        if event.type == KEYDOWN:       
            #按的键是否为退出
            if event.key == K_ESCAPE:
                running = False
        #鼠标点击事件
        elif event.type == QUIT:
            running = False            
    # 将图片surface对象绘制到窗口surface上
    screen.blit(pic,(200,200)) 
    #移动
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    screen.blit(player.surf, player.rect)  
    # 刷新屏幕
    pygame.display.update() 
    #打开显示器
    pygame.display.flip()
    pygame.event.pump()
pygame.quit()
