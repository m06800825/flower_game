import os
import pygame as pg
import time
import math
from utils import Player, Flower, Arrow


def main():
    pg.init()
    
    # music and sound
    sound_path = os.path.join("music", "sound.wav")
    music_path = os.path.join("music", "pacific.mp3")
    play_bg_music(music_path)

    # initialize game window
    canvas_width = 1200
    canvas_height = 750
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Anniversary Game")

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
    message_font = pg.font.SysFont("Arial", 60)
    menu_msg = "[PRESS SPACE TO CHOOSE PLAYER]"
    end_msg = ""
    start_msg = "[PRESS SPACE TO START]"

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
            menu_logo = message_font.render(menu_msg, True, (255, 0, 0))
            canvas.blit(menu_logo, (160, 650))
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
                    end_msg = "[TIME'S UP]"
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
                end_logo = message_font.render(end_msg, True, (0, 0, 255))
                start_logo = message_font.render(start_msg, True, (0, 0, 255))
                canvas.blit(end_logo, (480, 330))
                canvas.blit(start_logo, (300, 400))

        pg.display.update()

    pg.quit()
    quit()


def play_bg_music(music_path):
    # load music
    pg.mixer.music.load(music_path)
    # set volume
    pg.mixer.music.set_volume(0.5)
    # recursive playing
    pg.mixer.music.play(-1, 0)


def play_sound(sound_path):
    # load sound
    sound = pg.mixer.Sound(sound_path)
    # set volume
    sound.set_volume(0.3)
    # play
    sound.play()


def count_second(start_time):
    last_time = time.time()
    total_time = math.floor(last_time - start_time)
    return total_time


if __name__ == "__main__":
    main()