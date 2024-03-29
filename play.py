import os
import pygame as pg
import time
import math
import ctypes
from utils import Player, Flower, Arrow


def main():
    pg.init()

    # initialize taskbar icon
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    # music and sound
    sound_path = os.path.join("music", "sound.wav")
    music_path = os.path.join("music", "pacific.mp3")
    play_bg_music(music_path)

    # initialize game window
    canvas_width = 1200
    canvas_height = 750
    canvas = pg.display.set_mode((canvas_width, canvas_height), pg.FULLSCREEN)
    pg.display.set_caption("9th Anniversary Game")

    # initialize icon
    icon = pg.image.load(os.path.join('image', 'flower_removebg.png')).convert_alpha()
    icon = pg.transform.scale(icon, (30, 30))
    pg.display.set_icon(icon)

    # initialize group
    arrows = pg.sprite.Group()
    flowers = pg.sprite.Group()
    players = pg.sprite.Group()

    # initialize menu
    couple = pg.image.load(os.path.join('image', 'couple.png'))
    couple = pg.transform.scale(couple, (1200, 750))
    arrow = Arrow()
    arrows.add(arrow)
    

    # initialize background
    grassland = pg.image.load(os.path.join('image', 'grassland.png'))
    grassland = pg.transform.scale(grassland, (1200, 750))

    # initialize time
    clock = pg.time.Clock()
    start_time = time.time()
    sec = 0

    # initialize score
    score = 0

    # initialize game message
    score_font = pg.font.SysFont("Arial", 40)
    time_font = pg.font.SysFont("Arial", 40)

    # initialize game message
    menu_msg = pg.image.load(os.path.join('image', 'menu.png')).convert_alpha()
    menu_msg = pg.transform.scale(menu_msg, (1000, 100))
    start_msg = pg.image.load(os.path.join('image', 'start.png')).convert_alpha()
    start_msg = pg.transform.scale(start_msg, (600, 100))
    end_msg = pg.image.load(os.path.join('image', 'timeup.png')).convert_alpha()
    end_msg = pg.transform.scale(end_msg, (300, 100))

    # initialize game status
    running = True
    menu = True
    playing = False

    while running:
        clock.tick(30)

        if menu:
            for event in pg.event.get():
                # leave game
                if event.type == pg.QUIT:
                    running = False
                # check button down
                if event.type == pg.KEYDOWN:
                    # check ESC down
                    if event.key == pg.K_ESCAPE:
                        running = False
                    # change arrow location
                    if event.key == pg.K_LEFT:
                        arrow.update(380)
                    elif event.key == pg.K_RIGHT:
                        arrow.update(720)     
                    # choose player                 
                    if event.key == pg.K_SPACE and arrow.rect.x == 380:
                        player = Player("ken")
                        players.add(player)
                        menu = False
                    elif event.key == pg.K_SPACE and arrow.rect.x == 720:
                        player = Player("jane")
                        players.add(player)
                        menu = False

            canvas.blit(couple, (0,0))
            canvas.blit(menu_msg, (100, 650))
            arrows.draw(canvas)

        else:
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
                        player.speed = -20
                    elif event.key == pg.K_RIGHT:
                        player.speed = 20
                    elif event.key == pg.K_DOWN:
                        player.speed = 0
                    # start playing 
                    if event.key == pg.K_SPACE:
                        if not playing:
                            playing = True
                            flowers.empty()
                            # initailize
                            score = 0
                            player.speed = 0
                            player.rect.x = 525
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
                    f = Flower()
                    flowers.add(f)
                
                # detect collide
                hit_flower = pg.sprite.spritecollide(player, flowers, True)  
                if len(hit_flower) > 0:
                    play_sound(sound_path)
                    score += len(hit_flower)

                # update objects
                player.update()
                for flower in flowers:
                    flower.update()

            # update score
            score_msg = "Score: " + str(score)
            score_msg = score_font.render(score_msg, True, (255, 0, 0))

            # update time
            time_msg = "Time: " + str(30-sec)
            time_msg = time_font.render(time_msg, True, (255, 100, 0))

            # draw 
            canvas.blit(grassland, (0,0))
            canvas.blit(score_msg, (10, 10))
            canvas.blit(time_msg, (1050, 10))
            flowers.draw(canvas)
            players.draw(canvas)

            if not playing:
                # show message
                if sec == 30:
                    canvas.blit(end_msg, (450, 320))
                canvas.blit(start_msg, (300, 390))

        pg.display.update()

    pg.quit()
    quit()


def play_bg_music(music_path):
    pg.mixer.music.load(music_path)
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(-1, 0)


def play_sound(sound_path):
    sound = pg.mixer.Sound(sound_path)
    sound.set_volume(0.3)
    sound.play()


def count_second(start_time):
    last_time = time.time()
    total_time = math.floor(last_time - start_time)
    return total_time


if __name__ == "__main__":
    main()