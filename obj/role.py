import pygame as pg
import os

class Role(pg.sprite.Sprite):
    def __init__(self, name="ken"):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        if name == "jane":
            self.image = pg.image.load(os.path.join('image', 'jane_removebg.png')).convert_alpha ()
        else:
            self.image = pg.image.load(os.path.join('image', 'ken_removebg.png')).convert_alpha ()
        self.image = pg.transform.scale(self.image, (150, 200))
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
