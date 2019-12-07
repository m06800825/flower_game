import numpy as np
import cv2
import os, sys, random
import pygame as pg
import role.flower as flower
from pygame.locals import *

if __name__ == "__main__":
    pg.init()

    canvas_width = 1200
    canvas_height = 800
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Anniversary game")

    sky = pg.image.load("image\sky.jpg")
    sky = pg.transform.scale(sky, (1200, 800))

    canvas.blit(sky, (0,0))
    pg.display.update()

    clock = pg.time.Clock()
    font = pg.font.SysFont('simhei', 18)

    # 遊戲狀態.
    # 0:等待開球
    # 1:遊戲進行中
    game_mode = 0

    running = True
    while running:
        for event in pg.event.get():
            # 離開遊戲.
            if event.type == pg.QUIT:
                running = False
            # 判斷按下按鈕
            if event.type == pg.KEYDOWN:
                # 判斷按下ESC按鈕
                if event.key == pg.K_ESCAPE:
                    running = False
                
        # 判斷Mouse.
            if event.type == pg.MOUSEMOTION:
                paddle_x = pg.mouse.get_pos()[0] - 50
            if event.type == pg.MOUSEBUTTONDOWN:
                if(game_mode == 0):
                    game_mode = 1

        # canvas.fill(background)
        # canvas.blit(sky,(0,0))

        pg.display.update()
        clock.tick(60)

    pg.quit()
    quit()