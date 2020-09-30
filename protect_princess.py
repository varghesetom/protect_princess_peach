#!/usr/bin/env python

'''
Protect Princess Peach from the Koopas as she picks up flowers! 
'''

import pygame, random, sys, math, copy, time
from pygame.locals import *
import util
from Characters import Nintendo, Mario, Peach, KoopaArmy 
from Flower import Flower 
from settings import * 

## set up pygame, mouse, surface
pygame.init()
window_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Protect Princess Peach")
font = pygame.font.SysFont(None,30) # default font set at 30 points 
clock = pygame.time.Clock() ## time used to speed up the game with FPS 
pygame.mouse.set_visible = False 

# show start screen
sky = pygame.image.load(r"./images/sky.png") 
# pygame.display.update()

# set up images and characters 
mario = Mario(left=100, top =100, width = 40, height =40) 
peach = Peach(left=200, top=500, width=40, height=40)
flower = Flower(window_surface) 
koopa_army = KoopaArmy() 
koopa_add_counter = 0

## directional buttons and score 
topscore = 0
score = 0 
game_over = False 

def show_start_screen():
    pass

def show_game_over():
    window_surface.fill((255, 255, 255)) 
    util.draw_text("GAME OVER!", font, window_surface, window_width / 1.5, window_height / 1.5)
    util.draw_text("Press a key to begin", font, window_surface, window_width / 1.5, window_height *(3/4))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                util.terminate()  
            if event.type == pygame.KEYUP:
                waiting = False

# set up game loop 
while True:
    if game_over:
        show_game_over()
        game_over = False 
        score = 0 
        koopa_add_counter = 0 
        koopa_army.koopas = [] 

    ## go through event loop 
    for event in pygame.event.get():
        if event.type == QUIT:
            util.terminate()
    keys = pygame.key.get_pressed()  # better than using polling to get KEYDOWN events
    mario.move_left = keys[K_LEFT] and not keys[K_RIGHT]
    mario.move_right = keys[K_RIGHT] and not keys[K_LEFT]
    mario.move_up = keys[K_UP] and not keys[K_DOWN]
    mario.move_down = keys[K_DOWN] and not keys[K_UP] 
     
     ## go through game loop and add koopas 
    koopa_add_counter += 1 
    if koopa_add_counter == koopa_army.bad_rate:
        koopa_add_counter = 0
        koopa_army.generate_koopa(window_surface)  

    # draw game world 
    window_surface.fill(background)
    window_surface.blit(sky, (0,0)) 

    util.draw_text("Score : %s" % (score), font, window_surface, 450, 510)
    util.draw_text("Top Score : %s" % (topscore), font, window_surface, 450,540)
    
    # move characters  
    mario.move_and_attack(window_surface, koopa_army) 
    peach.move_towards(flower) 
    koopa_army.move(peach) 

    # draw updated_positions 
    mario.draw_character(window_surface)
    peach.draw_character(window_surface) 
    flower.draw_character(window_surface) 
    koopa_army.draw_army(window_surface) 

    pygame.display.update()

    ## check if Peach reach flower 
    if peach.did_reach_flower(flower):
        score += 1 
        flower = Flower(window_surface) 
    
    # check if koopa hit peach 
    if peach.got_captured_by(koopa_army): 
        game_over = True 
        if score > topscore:
            topscore = score 
    
    # setting game speed 
    clock.tick(fps)
    


