import pygame as pg
import os
import random

class Flower(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('image', 'flower_removebg.png')).convert_alpha ()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = int(random.random() * 1150)
        self.rect.y = 0

    def update(self):
        self.rect.y += 20
