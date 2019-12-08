import numpy as np
import cv2
import os, sys, random
import pygame as pg
import time
from role.flower import Flower
from role.role import Role
from pygame.locals import *

if __name__ == "__main__":
    pg.init()

    canvas_width = 1200
    canvas_height = 800
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Anniversary game")

    sky = pg.image.load(os.path.join('image', 'grassland.png'))
    sky = pg.transform.scale(sky, (1200, 800))

    role = Role("ken")

    clock = pg.time.Clock()
    start_time = time.time()
    font = pg.font.SysFont('simhei', 18)

    allsprite = pg.sprite.Group()
    allsprite.add(role)

    # 0: wait to begin
    # 1: game is running
    game_mode = 0
    flower_index = 0

    running = True
    while running:
        clock.tick(30)
        time_difference = int((time.time() - start_time) * 1000)
        
        # Flower
        if time_difference > 500:
            start_time += 0.5 # generate a flower per 0.5 second
            flower_index += 1
            f = Flower(flower_index)
            print('index:', flower_index)
            allsprite.add(f)


        for event in pg.event.get():
            # leave game
            if event.type == pg.QUIT:
                running = False
            # check button down
            if event.type == pg.KEYDOWN:
                # check ESC down
                if event.key == pg.K_LEFT:
                    role.speed = -20
                # check left and right
                elif event.key == pg.K_RIGHT:
                    role.speed = 20
                if event.key == pg.K_ESCAPE:
                    running = False
                
            # check mouse
            if event.type == pg.MOUSEBUTTONDOWN:
                if(game_mode == 0):
                    game_mode = 1
        
        # update objects
        role.update()
        for flower in allsprite:
            if hasattr(flower, 'index'):
                flower.update()

        canvas.blit(sky, (0,0))
        allsprite.draw(canvas)
        pg.display.update()

    pg.quit()
    quit()