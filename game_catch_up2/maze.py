import time
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
mixer.init()
# mixer.music.load("jungles.ogg")
# mixer.music.play()

kick = mixer.Sound("kick.ogg")
# kick.play()

money = mixer.Sound("money.ogg")
# money.play()

# Set up fonts text
pygame.font.init()
font = pygame.font.Font(None, 70)
win_text = font.render("YOU WIN", True, (255, 215, 0))
lose_text = font.render("GAME OVER", True, (180, 215, 0))

# create 2 sprites and place them on the scene
class GameSprite(sprite.Sprite):
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
    def __init__(self, window, image, x, y, speed, width=65, height=65):
        super().__init__(window, image, x, y, speed, width, height)

        self.w = 80
        self.h = 100
        self.rx = randint(-10, 10)
        self.ry = randint(-10, 10)

        self.rx = 1

    def move(self):

        self.x += self.rx * self.speed
        # self.y += self.ry*self.speed

    @GameSprite.x.setter
    def x(self, v):
        if self.x_org - self.w < v < self.x_org + self.w:
            self.rect.x = v
        else:
            self.rx *= -1

    @GameSprite.y.setter
    def y(self, v):
        if self.y_org - self.h < v < self.y_org + self.h:
            self.rect.y = v
        else:
            self.rx = randint(-1, 1)
            self.ry = randint(-1, 1)

            while self.rx == self.ry == 0:
                self.rx = randint(-1, 1)
                self.ry = randint(-1, 1)


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

player = Player(window, "hero.png", 25, 100, 5)
enemy = Enemy(window, "cyborg.png", 530, 250, 2)
treasure = GameSprite(window, "treasure.png", 530, 430, 0)

walls = [wall1, wall2, wall3, wall4, enemy]

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
    player.draw()
    enemy.draw()
    wall1.draw()
    wall2.draw()
    wall3.draw()
    wall4.draw()
    treasure.draw()

    player.move()
    enemy.move()

    for wall in walls:
        if pygame.sprite.collide_rect(player, wall):
            kick.play()
            player.reset()
            window.blit(lose_text, (200, 200))
            pygame.display.update()
            time.sleep(5)

            # while True:
            #
            #     key_pressed = pygame.key.get_pressed()
            #
            #     if key_pressed[pygame.K_a]:
            #         print("Heli")
            #         break
            #
            #     pygame.display.update()
            #     clock.tick(FPS)


    if pygame.sprite.collide_rect(player, treasure):
        money.play()
        window.blit(win_text, (200, 200))
        run = False

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

run = True
while run:
    pygame.display.update()
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

pygame.display.quit()
