# from pygame import *
import pygame

pygame.init()

#create game window
pygame.display.set_caption("Catch")
window = pygame.display.set_mode((700, 500))
window.fill((80, 80, 80))

#set scene background
background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))

#creat 2 sprites and place them on the scene
sprite1 = pygame.transform.scale(pygame.image.load("sprite1.png"), (100, 100))
sprite2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (100, 100))

x1 = 100
y1 = 100

x2 = 200
y2 = 100


clock = pygame.time.Clock()
FPS = 60

run = True

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_a] and x1 > 0:
        x1 -= 10
    if key_pressed[pygame.K_d] and x1 < 600:
        x1 += 10
    if key_pressed[pygame.K_w] and y1 > 0:
        y1 -= 10
    if key_pressed[pygame.K_s] and y1 < 400:
        y1 += 10

    if key_pressed[pygame.K_LEFT]:
        x2 -= 10
    if key_pressed[pygame.K_RIGHT]:
        x2 += 10
    if key_pressed[pygame.K_UP]:
        y2 -= 10
    if key_pressed[pygame.K_DOWN]:
        y2 += 10

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()
