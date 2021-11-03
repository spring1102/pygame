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
# 窗口宽高
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#用Boolean进入或退出循环
running = True
while running:
    for event in pygame.event.get():
        #键盘：是否按了键
        if event.type == KEYDOWN:
            #按的键是否为退出
            if event.key == K_ESCAPE:
                running = False
        #鼠标点击事件
        elif event.type == QUIT:
            running = False
pygame.quit()
