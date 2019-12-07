import pygame as pg
import os

class Flower(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('image', 'flower_removebg.png')).convert_alpha ()
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

    def update(self):  
        pos = pg.mouse.get_pos()  
        self.rect.x = pos[0]       #滑鼠x坐標
        #不要移出右邊界
        # if self.rect.x > canvas.get_width() - self.rect.width:
        #     self.rect.x = canvas.get_width() - self.rect.width
