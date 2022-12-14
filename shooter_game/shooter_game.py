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
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
#
fire = mixer.Sound("fire.ogg")
# kick.play()

# # Set up fonts text
pygame.font.init()
font = pygame.font.Font(None, 70)
win_text = font.render("YOU WIN", True, (255, 215, 0))
lose_text = font.render("GAME OVER", True, (180, 215, 0))

font_score = pygame.font.Font(None, 32)


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

    def __iter__(self):
        return self.bullets.__iter__()

    def remove(self, v):
        self.bullets.remove(v)

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
            fire.play()

    def draw(self):
        super().draw()

        for bullet in self.bullets:
            bullet.update()
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

    def update(self):
        self.move_up()

    def draw(self):
        super().draw()

    @GameSprite.y.setter
    def y(self, v):
        if 0 < v < self.window.get_height() - self.height:
            self.rect.y = v
        else:
            self.destroy = True


class Enemy(GameSprite):
    def draw(self):
        if not self.destroy:
            self.move_down()
            super().draw()

    @GameSprite.y.setter
    def y(self, v):
        if v < self.window.get_height() - self.height:
            self.rect.y = v
        else:
            self.destroy = True


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


class EnemyHandler:
    def __init__(self, N):
        self.enemies = []
        self.N = N
        self.miss_ufo = 0

    def __getitem__(self, item):
        return self.enemies[item]

    def __iter__(self):
        return self.enemies.__iter__()

    def remove(self, v):
        self.enemies.remove(v)

    def max_check(self):
        max = 0

        if len(self.enemies) == 0:
            return True

        for e in self.enemies:
            if max < e.y:
                max = e.y

        return max > 200

    def spawn(self):
        if not self.max_check():
            return

        N = len(self.enemies)
        r = randint(0, self.N - N)

        for _ in range(r):
            x = randint(100, 600)
            speed = randint(1, 3)
            enemy = Enemy(window, "ufo.png", x, -65, speed, 100, 65)

            for e in self.enemies:
                if pygame.sprite.collide_rect(enemy, e):
                    break
            else:
                self.enemies.append(enemy)

    def draw(self):
        self.spawn()

        for e in self.enemies:
            e.draw()
            if e.destroy:
                self.miss_ufo += 1
                print(f"{self.miss_ufo=}")
                self.enemies.remove(e)


wall1 = Wall(window, 100, 20, 10, 350, (154, 205, 50))
wall2 = Wall(window, 220, 120, 10, 350, (154, 205, 50))
wall3 = Wall(window, 340, 20, 10, 350, (154, 205, 50))
wall4 = Wall(window, 440, 120, 10, 350, (154, 205, 50))

player = Player(window, "rocket.png", 350 - 65 // 2, 400, 5)
# enemy = Enemy(window, "ufo.png", 330, -200, 2, 100, 65)
enemies = EnemyHandler(6)

# Game variable
# miss_ufo = 0
score = 0

clock = pygame.time.Clock()
FPS = 60

run = True
while run:
    window.blit(background, (0, 0))


    player.move()
    player.draw()

    enemies.draw()

    # collide

    for b in player:
        for e in enemies:
            if pygame.sprite.collide_rect(b, e):
                player.remove(b)
                enemies.remove(e)
                score += 1
                print(f"{score=}")
                break

    score_txt = font_score.render(f"score: {score}", True, (255, 255, 255))
    miss_ufo_txt = font_score.render(f"miss: {enemies.miss_ufo}", True, (255, 255, 255))

    window.blit(score_txt, (10, 10))
    window.blit(miss_ufo_txt, (10, 30))

    if score == 10:
        window.blit(win_text, (200, 300))
        run = False

    if enemies.miss_ufo == 5:
        window.blit(lose_text, (200, 300))
        # run = False
        enemies.miss_ufo = 0
        score = 0
        enemies.enemies.clear()
        player.bullets.clear()
        pygame.time.delay(2000)

    # handle "click on the "Close the window"" event
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

# pygame.display.update()

while True:
    time.sleep(1)
