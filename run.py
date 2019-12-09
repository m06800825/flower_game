import os
import pygame as pg
import time
import math
from obj.flower import Flower
from obj.role import Role


def count_second(start_time):
    last_time = time.time()
    total_time = math.floor(last_time - start_time)
    return total_time


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


if __name__ == "__main__":
    pg.init()
    
    # music and sound
    sound_path = os.path.join("music", "sound.wav")
    music_path = os.path.join("music", "pacific.mp3")
    play_bg_music(music_path)

    # initialize game window
    canvas_width = 1200
    canvas_height = 750
    canvas = pg.display.set_mode((canvas_width, canvas_height))
    pg.display.set_caption("Catch Flower Game")

    # initialize background
    grassland = pg.image.load(os.path.join('image', 'grassland.png'))
    grassland = pg.transform.scale(grassland, (1200, 750))

    # initialize time
    clock = pg.time.Clock()
    start_time = time.time()
    sec = 0

    # initialize group
    flowers = pg.sprite.Group()
    roles = pg.sprite.Group()
    role = Role("ken")
    roles.add(role)

    # initialize score
    score = 0

    # initialize game message
    score_font = pg.font.SysFont("Arial", 40)
    time_font = pg.font.SysFont("Arial", 40)
    message_font = pg.font.SysFont("Arial", 60)
    end_msg = ""
    start_msg = "[PRESS SPACE TO START]"

    # initialize game status
    playing = False
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
                        flowers.empty()
                        # initailize
                        score = 0
                        role.speed = 0
                        role.rect.x = 525
                        start_time = time.time()
                        gen_flower_time = time.time()
        
        if playing:
            sec = count_second(start_time)
            if sec == 30:
                end_msg = "[GAME OVER]"
                playing = False

            time_difference = int((time.time() - gen_flower_time) * 1000)
            # Flower
            if time_difference > 500:
                gen_flower_time += 0.5 # generate a flower per 0.5 second
                f = Flower()
                flowers.add(f)
            
            # detect collide
            hit_flower = pg.sprite.spritecollide(role, flowers, True)  
            if len(hit_flower) > 0:
                play_sound(sound_path)
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
        time_msg = time_font.render(time_msg, True, (255, 100, 0))

        canvas.blit(grassland, (0,0))
        canvas.blit(score_msg, (10, 10))
        canvas.blit(time_msg, (1050, 10))
        flowers.draw(canvas)
        roles.draw(canvas)

        if not playing:
            end_logo = message_font.render(end_msg, True, (0, 0, 255))
            start_logo = message_font.render(start_msg, True, (0, 0, 255))
            canvas.blit(end_logo, (450, 330))
            canvas.blit(start_logo, (300, 400))

        pg.display.update()

    pg.quit()
    quit()