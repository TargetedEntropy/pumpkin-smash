import pygame
import sys

pygame.init()
windowSize = (800,600)

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("head.png")
backGround = pygame.image.load("bg.png")
pumpkin = pygame.image.load("pumpkin.png")
powPic = pygame.image.load("pow.png")

helloWorldSize = helloWorld.get_size()
pumpkinSize = pumpkin.get_size()
pygame.mouse.set_visible(0)

x, y = 0,0
directionX, directionY = 1, 1

pump_x, pump_y = 0,0
pump_dir_x, pump_dir_y = 1, 1

clock = pygame.time.Clock()

while 1:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0,0, 0))
    screen.blit(backGround, (0,0))
    screen.blit(pumpkin, (pump_x,pump_y))
    mousePoition = pygame.mouse.get_pos()
     
    x, y = mousePoition
    screen.blit(helloWorld, (x, y))

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]        

    pump_x += 5 * pump_dir_x
    pump_y += 5 * pump_dir_y

    if pump_x> 800 or pump_x <= 0:
        pump_dir_x *= -1

    if pump_y > 600 or pump_y <= 0:
        pump_dir_y *= -1

    if pump_x - x < 2 and pump_y - y < 23:
        screen.blit(powPic, (x, y))

    pygame.display.update()