# from pygame import *
import pygame
from pygame import mixer, sprite

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
    def move(self):
        pass

sprite1 = Player(window, "hero.png", 100, 100, 10)
sprite2 = Enemy(window, "cyborg.png", 100, 200, 10)

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

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # key_pressed = pygame.key.get_pressed()
    #
    # if key_pressed[pygame.K_a]:
    #     sprite1.move_left()
    # if key_pressed[pygame.K_d]:
    #     sprite1.move_right()
    # if key_pressed[pygame.K_w]:
    #     sprite1.move_up()
    # if key_pressed[pygame.K_s]:
    #     sprite1.move_down()
    #
    # if key_pressed[pygame.K_LEFT]:
    #     sprite2.move_left()
    # if key_pressed[pygame.K_RIGHT]:
    #     sprite2.move_right()
    # if key_pressed[pygame.K_UP]:
    #     sprite2.move_up()
    # if key_pressed[pygame.K_DOWN]:
    #     sprite2.move_down()

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()
