import numpy as np
import cv2
import os, sys, random
import pygame as pg
from role.flower import Flower
from role.jane import Jane
from pygame.locals import *

if __name__ == "__main__":
    pg.init()

    canvas_width = 1200
    canvas_height = 800
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Anniversary game")

    sky = pg.image.load(os.path.join('image', 'sky.jpg'))
    sky = pg.transform.scale(sky, (1200, 800))

    jane = Jane()

    clock = pg.time.Clock()
    font = pg.font.SysFont('simhei', 18)

    allsprite = pg.sprite.Group()
    allsprite.add(jane)

    # 0: wait to begin
    # 1: game is running
    game_mode = 0

    running = True
    while running:
        clock.tick(30)
        for event in pg.event.get():
            # leave game
            if event.type == pg.QUIT:
                running = False
            # check button down
            if event.type == pg.KEYDOWN:
                # check ESC down
                if event.key == pg.K_ESCAPE:
                    running = False
                
        # 判斷Mouse.
            if event.type == pg.MOUSEMOTION:
                paddle_x = pg.mouse.get_pos()[0] - 50
            if event.type == pg.MOUSEBUTTONDOWN:
                if(game_mode == 0):
                    game_mode = 1

        jane.update()

        canvas.blit(sky, (0,0))
        allsprite.draw(canvas)
        pg.display.update()

    pg.quit()
    quit()