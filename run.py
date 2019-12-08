import numpy as np
import cv2
import os, sys, random
import pygame as pg
import time
import math
from obj.flower import Flower
from obj.role import Role
from pygame.locals import *

def count_second(start_time):
    last_time = time.time()
    total_time = math.floor(last_time - start_time)
    return total_time


if __name__ == "__main__":
    pg.init()

    canvas_width = 1200
    canvas_height = 800
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Anniversary game")

    clock = pg.time.Clock()
    start_time = time.time()
    score_font = pg.font.SysFont("Arial", 40)
    time_font = pg.font.SysFont("Arial", 40)
    start_font = pg.font.SysFont("Arial", 60)

    sky = pg.image.load(os.path.join('image', 'grassland.png'))
    sky = pg.transform.scale(sky, (1200, 800))
    role = Role("jane")

    flowers = pg.sprite.Group()
    allsprite = pg.sprite.Group()
    allsprite.add(role)

    playing = False
    flower_index = 0
    score = 0
    sec = 0

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
                # check left and right
                if event.key == pg.K_LEFT:
                    role.speed = -20
                elif event.key == pg.K_RIGHT:
                    role.speed = 20
                elif event.key == pg.K_DOWN:
                    role.speed = 0
                # start playing 
                if event.key == pg.K_SPACE:
                    if not playing:
                        playing = True
                        score = 0
                        role.speed = 0
                        start_time = time.time()
                        gen_flower_time = time.time()
        
        if playing:
            sec = count_second(start_time)
            if sec == 30:
                playing = False

            time_difference = int((time.time() - gen_flower_time) * 1000)
            # Flower
            if time_difference > 500:
                gen_flower_time += 0.5 # generate a flower per 0.5 second
                flower_index += 1
                f = Flower(flower_index)
                flowers.add(f)
            
            # detect collide
            hit_flower = pg.sprite.spritecollide(role, flowers, True)  
            if len(hit_flower) > 0:
                score += len(hit_flower)

            # update objects
            role.update()
            for flower in flowers:
                flower.update()

        # update score
        score_msg = "Score: " + str(score)
        score_msg = score_font.render(score_msg, True, (255, 0, 0))

        # update time
        time_msg = "Time: " + str(30-sec)
        time_msg = time_font.render(time_msg, True, (255, 0, 0))

        canvas.blit(sky, (0,0))
        canvas.blit(score_msg, (10, 10))
        canvas.blit(time_msg, (1050, 10))
        flowers.draw(canvas)
        allsprite.draw(canvas)

        if not playing:
            start_msg = "[PRESS SPACE TO START]"
            start_msg = start_font.render(start_msg, True, (0, 0, 255))
            canvas.blit(start_msg, (300, 400))

        pg.display.update()

    pg.quit()
    quit()