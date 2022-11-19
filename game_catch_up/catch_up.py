# from pygame import *
import pygame

pygame.init()

# create game window
pygame.display.set_caption("Catch")
window = pygame.display.set_mode((700, 500))
window.fill((80, 80, 80))

# set scene background
background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))


# create 2 sprites and place them on the scene
class Player:
    def __init__(self, player_image, playerID, *, x=100, y=100):
        self.player_image = player_image
        self.playerID = playerID
        self.sprite = pygame.transform.scale(pygame.image.load(player_image), (100, 100))
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y


# sprite1 = pygame.transform.scale(pygame.image.load("sprite1.png"), (100, 100))
# sprite2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (100, 100))

sprite1 = Player("sprite1.png", 1, x=100, y=100)
sprite2 = Player("sprite2.png", 2, x=200, y=100)

x1 = 100
y1 = 100

x2 = 200
y2 = 100

clock = pygame.time.Clock()
FPS = 60

run = True

while run:
    window.blit(background, (0, 0))
    window.blit(sprite1.sprite, sprite1.pos)
    window.blit(sprite2.sprite, sprite2.pos)

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_a] and sprite1.x > 0:
        sprite1.x -= 10
    if key_pressed[pygame.K_d] and sprite1.x < 600:
        sprite1.x += 10
    if key_pressed[pygame.K_w] and sprite1.y > 0:
        sprite1.y -= 10
    if key_pressed[pygame.K_s] and sprite1.y < 400:
        sprite1.y += 10

    if key_pressed[pygame.K_LEFT] and x2 > 0:
        x2 -= 10
    if key_pressed[pygame.K_RIGHT] and x2 < 600:
        x2 += 10
    if key_pressed[pygame.K_UP] and y2 > 0:
        y2 -= 10
    if key_pressed[pygame.K_DOWN] and y2 < 400:
        y2 += 10

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()
