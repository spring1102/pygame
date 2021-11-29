#添加多个不同的图像
import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 0))
    #圆
    pygame.draw.circle(screen, (0, 255, 255), (75, 75), 75)
    #矩形
    pygame.draw.rect(screen, (0, 255, 255), (280, 10, 200, 100),0)
    #椭圆
    pygame.draw.ellipse(screen, (0, 255, 255), (10, 380,200,100), 1)
    #正方形
    pygame.draw.rect(screen, (0, 255, 255), (380, 380,100,100),0)
    #打开显示器
    pygame.display.flip()
pygame.quit()
