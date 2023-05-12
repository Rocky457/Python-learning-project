import pygame as pg
import time
import random
import sys
import os
import math
from os.path import isfile, join

#Initializing the pygame
pg.init()

# window
screen = pg.display.set_mode((800, 800))
pg.display.set_caption(" )_)  ''CAR RACER'' )_) ")

# loading images
#car_path = join("assets", "cars", "car-truck1.png")
#car1 = pg.image.load(car_path).convert_alpha()
car1 = pg.image.load("car_truck1.png")
clock = pg.time.Clock()
grass = pg.image.load("assets/background/Seamless.jpg")
#grass = ImageCms.profileToProfile(grass, "color/AdobeRGB1998.icc", "color/sRGB.icc")
y_strip = pg.image.load("yellow.png")
strip = pg.image.load("white.png")
start = pg.image.load("assets/background/city.png")


# function for getting all images
def background():
    screen.blit(grass, (0, 0))
    #screen.blit(grass, (700, 0))
    #screen.blit(y_strip, (400, 0))
    #screen.blit(y_strip, (400, 100))
    #screen.blit(y_strip, (400, 200))
    #screen.blit(y_strip, (400, 300))
    #screen.blit(y_strip, (400, 400))
    #screen.blit(y_strip, (400, 500))
    #screen.blit(y_strip, (400, 600))
    #screen.blit(strip, (120, 0))
    #screen.blit(strip, (680, 0))


# getting the cars
def car(x, y):
    screen.blit(car1, (x, y))


x_change = 0
x = 400
y = 470
car_width = 56
op_speed = 1
obs = 0
y_change = 0
obs_x = random.randrange(200, 650)
obs_y = -750
op_width = 56
op_height = 125
car_passed = 0
score = 0
level = 0


# function for enemy cars
def obstacle(obs_x, obs_y, obs):
    obs_img1 = pg.image.load("assets/cars/car-truck2.png")
    obs_img2 = pg.image.load("assets/cars/car-truck3.png")
    obs_img3 = pg.image.load("assets/cars/car-truck4.png")
    obs_img4 = pg.image.load("assets/cars/car-truck5.png")
    obs_img5 = pg.image.load("assets/cars/car-truck1.png")
    obs_img = obs_img1

    if obs == 0:
        obs_img = obs_img1
    elif obs == 1:
        obs_img = obs_img2
    elif obs == 2:
        obs_img = obs_img3
    elif obs == 3:
        obs_img = obs_img4
    elif obs == 4:
        obs_img = obs_img5
    screen.blit(obs_img, (obs_x, obs_y))




 # Message to displa
font = pg.font.SysFont("None", 150)
render = font.render("<< >> << >> CAR CRASHED << >> << >> ", True, (0, 0, 0))


 # Function to display score
def sc(car_passed, score):
     s_font = pg.font.SysFont(None, 35)
     passed = s_font.render("Passed:" + str(car_passed), True, (0, 0, 0))
     score = s_font.render("Score:" + str(score), True, (0, 0, 0))
     screen.blit(passed, (0, 30))
     screen.blit(score, (0, 70))


# Text on Buttons
def text(text, font):
    texts = font.render(text, True, (255, 255, 255))
    return texts, texts.get_rect()


# Game main loop
def game_loop():
    global op_speed, x, car_passed, level, x_change, y_change, y, obs_y, obs_x, obs, score, font, obs_height
    running = True
    while running:

        # for checking the events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change = -5
                if event.key == pg.K_RIGHT:
                    x_change = 5
                if event.key == pg.K_s: #speed UP
                    op_speed += 2
                if event.key == pg.K_b: #slow down
                    op_speed -= 3
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0

        x += x_change
        screen.fill((119, 119, 119))
        background()
        obs_y -= (op_speed / 4)
        obstacle(obs_x, obs_y, obs)
        obs_y += op_speed
        car(x, y)
        sc(car_passed, score)
        # Restricting the movement
        if x > 680 - car_width or x < 600:
            obs_y = 0 - op_height
            obs_x = random.randrange(170, 600)
            obs = random.randrange(0, 6)
            car_passed += 1
            score = car_passed * 10   # Score
            if int(car_passed) % 10 == 0:
                level += 1
                op_speed += 1   # increase enemy speed per level
                font = pg.font.SysFont(None, 50)
                level_text = font.render("Level" + str(level), True, (0, 0, 0))
                screen.blit(level_text, (0, 100))
                pg.display.flip()
        # car crash logic
            if y < obs_y + op_height and y + car_height > obs_y and x < obs_x + obs_width and x + car_width > obs_x and x + car_width < 80 and mouse[0] > 490 and mouse[0] < 580 and mouse[1] > 490 and mouse[1] < 590:
                pg.draw.rect(screen, (255, 0, 0), (580, 540, 150, 50))
            #if click == (1, 0, 0):
            #   pg.quit()
        t = pg.font.SysFont( "arial", 30)
        texts, textr = text("START", t)
        textr.center = ((80 + (150 / 2)), (540 + (50 / 2)))
        screen.blit(texts, textr)
        texts, textr = text("QUIT", t)
        textr.center = ((580 + (150 / 2)), (540 + (50 /2)))
        screen.blit(texts, textr)
        pg.display.update()

#intro() # calling the intro function
game_loop() # calling the game loop
pg.quit()
