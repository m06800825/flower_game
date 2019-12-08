import pygame as pg
import os

class Jane(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('image', 'jane_removebg.png')).convert_alpha ()
        self.image = pg.transform.scale(self.image, (150, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 525
        self.rect.y = 600
        self.speed = 0

    def update(self):
        self.rect.x += self.speed       #滑鼠x坐標
        # 不要移出右邊界
        if self.rect.x > (1200 - self.rect.width):
            self.rect.x = 1200 - self.rect.width
        elif self.rect.x < 0:
            self.rect.x = 0
