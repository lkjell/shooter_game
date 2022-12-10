# Create your own shooter

import time
# from pygame import *
import pygame
from pygame import mixer, sprite
from random import randint

pygame.init()

# create game window
pygame.display.set_caption("Shooter")
window = pygame.display.set_mode((700, 500))
window.fill((80, 80, 80))

# set scene background
background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (700, 500))


# Set up background sound
# mixer.init()
# mixer.music.load("space.ogg")
# mixer.music.play()
#
# fire = mixer.Sound("fire.ogg")
# kick.play()

# # Set up fonts text
# pygame.font.init()
# font = pygame.font.Font(None, 70)
# win_text = font.render("YOU WIN", True, (255, 215, 0))
# lose_text = font.render("GAME OVER", True, (180, 215, 0))


# create 2 sprites and place them on the scene
class GameSprite(sprite.Sprite):
    destroy = False

    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__()

        self.x_org = x
        self.y_org = y

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
        else:
            self.destroy = True

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def reset(self):
        self.x = self.x_org
        self.y = self.y_org

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed


class Player(GameSprite):
    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__(window, image, x, y, speed, width, height)
        self.bullets = []
        self.fire_guard = False

    def move(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a]:
            self.move_left()
        if key_pressed[pygame.K_d]:
            self.move_right()
        # if key_pressed[pygame.K_w]:
        #     self.move_up()
        # if key_pressed[pygame.K_s]:
        #     self.move_down()
        if key_pressed[pygame.K_SPACE]:
            self.fire()
            self.fire_guard = True
        else:
            self.fire_guard = False

    def fire(self):
        bsizex = 10
        bsizey = 10
        x = self.x + self.width // 2 - bsizex // 2 + 1
        if not self.fire_guard:
            self.bullets.append(Bullet(window, "bullet.png", x, self.y, 5, bsizex, bsizey))

    def draw(self):
        super().draw()

        for bullet in self.bullets:
            bullet.draw()
            if bullet.destroy:
                self.bullets.remove(bullet)

        # try:
        #     self.bullet.draw()
        # except AttributeError:
        #     pass


key_pressed = pygame.key.get_pressed()


class Bullet(GameSprite):
    # destroy = False

    # def __init__(self, window, image, x, y, speed, width=10, height=10):
    #     super().__init__(window, image, x, y, speed, width, height)
    #     self.destroy = False

    def draw(self):
        self.move_up()
        super().draw()

    @GameSprite.y.setter
    def y(self, v):
        if 0 < v < self.window.get_height() - self.height:
            self.rect.y = v
        # else:
        #     self.destroy = True


class Enemy(GameSprite):
    # destroy = False

    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__(window, image, x, y, speed, width, height)

    def draw(self):
        if not self.destroy:
            self.move_down()
            super().draw()

    @GameSprite.y.setter
    def y(self, v):
        if 0 < v < self.window.get_height() - self.height:
            self.rect.y = v
        # else:
        #     self.destroy = True


class Wall(sprite.Sprite):
    def __init__(self, window, x, y, w, h, color, show=True):
        super().__init__()
        self.window = window
        self.wall = pygame.Surface((w, h))
        self.wall.fill(color)
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.show = show

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    def draw(self):
        if self.show:
            self.window.blit(self.wall, (self.x, self.y))


wall1 = Wall(window, 100, 20, 10, 350, (154, 205, 50))
wall2 = Wall(window, 220, 120, 10, 350, (154, 205, 50))
wall3 = Wall(window, 340, 20, 10, 350, (154, 205, 50))
wall4 = Wall(window, 440, 120, 10, 350, (154, 205, 50))

player = Player(window, "rocket.png", 350 - 65 // 2, 400, 5)
enemy = Enemy(window, "ufo.png", 330, 50, 2, 100, 65)

x1 = 100
y1 = 100

x2 = 200
y2 = 100

clock = pygame.time.Clock()
FPS = 60

run = True
i = 1
while run:
    window.blit(background, (0, 0))
    player.move()
    player.draw()

    enemy.draw()

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)
