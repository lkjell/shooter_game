# from pygame import *
import pygame
from pygame import mixer, sprite
from random import randint

pygame.init()

# create game window
pygame.display.set_caption("Catch")
window = pygame.display.set_mode((700, 500))
window.fill((80, 80, 80))

# set scene background
background = pygame.transform.scale(pygame.image.load("background.jpg"), (700, 500))


# Set up background sound
# mixer.init()
# mixer.music.load("jungles.ogg")
# mixer.music.play()

# kick = mixer.Sound("kick.ogg")
# kick.play()

# money = mixer.Sound("money.ogg")
# money.play()

# create 2 sprites and place them on the scene
class GameSprite(sprite.Sprite):
    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__()

        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(image), (self.width, self.height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window  # Parent

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, v):
        if 0 < v < self.window.get_width() - self.width:
            self.rect.x = v

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, v):
        if 0 < v < self.window.get_height() - self.height:
            self.rect.y = v

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed


class Player(GameSprite):
    def move(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            self.move_left()
        if key_pressed[pygame.K_d]:
            self.move_right()
        if key_pressed[pygame.K_w]:
            self.move_up()
        if key_pressed[pygame.K_s]:
            self.move_down()


class Enemy(GameSprite):
    direction = "right"

    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__(window, image, x, y, speed, width, height)

        self.x_org = x
        self.y_org = y
        self.w = 100
        self.h = 100
        self.rx = randint(-1, 1)
        self.ry = randint(-1, 1)

    def move(self):

        self.x += self.rx*self.speed
        print(self.x)
        # self.y += self.ry*self.speed

        # if self.direction == "right":
        #     self.move_right()
        # if self.direction == "left":
        #     self.move_left()
        # if self.direction == "up":
        #     self.move_up()
        # if self.direction == "down":
        #     self.move_down()

    @GameSprite.x.setter
    def x(self, v):
        if self.x_org - self.w < v < self.x_org + self.w:
            self.rect.x = v
        else:
            self.rx = randint(-1, 1)
            self.ry = randint(-1, 1)

        # if 0 < v < self.window.get_width() - self.width:
        #     self.rect.x = v
        # else:
        #     if self.direction == "left":
        #         self.direction = "right"
        #     elif self.direction == "right":
        #         self.direction = "left"

    @GameSprite.y.setter
    def y(self, v):
        if self.y_org - self.h < v < self.y_org + self.h:
            self.rect.x = v
        else:
            self.rx = randint(-1, 1)
            self.ry = randint(-1, 1)

        # if 0 < v < self.window.get_height() - self.height:
        #     self.rect.y = v
        # else:
        #     pass


sprite1 = Player(window, "hero.png", 100, 100, 10)
sprite2 = Enemy(window, "cyborg.png", 530, 250, 1)

x1 = 100
y1 = 100

x2 = 200
y2 = 100

clock = pygame.time.Clock()
FPS = 60

run = True

while run:
    window.blit(background, (0, 0))
    sprite1.draw()
    sprite2.draw()

    sprite1.move()
    sprite2.move()

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()
