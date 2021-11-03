#练习
import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    #1.修改第二个变量，改变颜色
    #2.修改第三个变量，定位到左上角
    pygame.draw.circle(screen, (0, 255, 255), (75, 75), 75)
    pygame.display.flip()
pygame.quit()
