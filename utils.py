import pygame as pg
import os
import random


class Player(pg.sprite.Sprite):
    def __init__(self, name="ken"):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        if self.name == "jane":
            self.image = pg.image.load(os.path.join('image', 'jane_removebg.png')).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join('image', 'ken_removebg.png')).convert_alpha()
        self.image = pg.transform.scale(self.image, (125, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 525
        self.rect.y = 550
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        # check not to exceed canvas
        if self.rect.x > (1200 - self.rect.width):
            self.rect.x = 1200 - self.rect.width
        elif self.rect.x < 0:
            self.rect.x = 0


class Flower(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('image', 'flower_removebg.png')).convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = int(random.random() * 1150)
        self.rect.y = 0

    def update(self):
        self.rect.y += 20


class Arrow(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('image', 'arrow_removebg.png')).convert_alpha()
        self.image = pg.transform.scale(self.image, (80, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 380
        self.rect.y = 20
    
    def update(self, x_loc):
        self.rect.x = x_loc