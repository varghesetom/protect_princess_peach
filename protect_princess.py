#!/usr/bin/env python

'''
Protect Princess Peach from the Koopas as she picks up flowers! 
'''

import pygame, random, sys, math, copy, time
from Characters import Nintendo, Mario, Peach 

from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()
    
#Use the [:] to create a copy so as not to mess up the other processes of adding koopas 

def did_koopa_reach_peach():
    for k in koopas:
        if peach.body.colliderect(k["rect"]):
            return True 
    return False  

def mario_removes_koopa():
    for k in koopas[:]:
        if mario.hit_koopa(k):
            koopas.remove(k)

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, text_color)  ## defining the text object with font and color 
    textrect = textobj.get_rect() # getting size and location of this text object 
    textrect.topleft = (x,y) ## setting the location of the text object 
    surface.blit(textobj, textrect) ## displaying the textobject at the text location 
    
def generateKoopa():
    koopaSize = random.randint(koopa_minsize, koopa_maxsize)
    north_south = [(0.200), (window_height-koopaSize)]
    # Rect -> left, top, width, height attributes
    new_koopa = {"rect" : pygame.Rect(random.randint(0, window_width - koopaSize), random.randint(0,200), koopaSize, koopaSize), #random.choice(north_south)
                 "speed" : random.randint(koopa_minspeed, koopa_maxspeed), 
                 "surface" : pygame.transform.scale(koopaImage, (koopaSize, koopaSize))}
    koopas.append(new_koopa)
    return koopas

def moveKoopa(koopa, peach):
    dx, dy = koopa["rect"].x - peach.x, koopa["rect"].y - peach.y
    dist = math.hypot(dx, dy) # euclidean distance
    dx, dy = dx/dist, dy/dist ## normalize distance magnitude so koopas won't move super fast 
    koopa["rect"].x -= dx * random.randint(koopa_minspeed, koopa_maxspeed)
    koopa["rect"].y -= dy * random.randint(koopa_minspeed, koopa_maxspeed)
    
## set up pygame, mouse, surface
pygame.init()
window_width = 600
window_height = 600 
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption("Protect Princess Peach")
mainClock = pygame.time.Clock() ## time used to speed up the game with FPS 
pygame.mouse.set_visible = False 
window_width = 900
window_height = 900 
text_color = (0,0,0)
background = (0,255,255) 
fps = 40 
font = pygame.font.SysFont(None,30) # default font set at 30 points 
# show start screen
window_surface.fill(background)
drawText("Protect Princess Peach!" , font, window_surface, window_width/2, window_height/2)
pygame.display.update()

# set up images and characters 
mario = Mario(left=100, top =100, width = 40, height =40) 
peach = Peach(left=200, top=500, width=40, height=40)

## koopa characteristics 
koopas = []
koopaImage = pygame.image.load("images/koopa.bmp")
koopa_minsize = 30
koopa_maxsize = 40
koopa_minspeed = 1 
koopa_maxspeed = 5 
koopa_bad_rate = 5
koopa_add = 0

## directional buttons and score 
topscore = 0
score = 0 

# set up game loop 
while True:
    score += 1
    ## go through event loop 
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                mario.move_left = True 
                mario.move_right = False 
            if event.key == K_RIGHT:
                mario.move_right = True
                mario.move_left = False 
            if event.key == K_UP:
                mario.move_up = True 
                mario.move_down = False 
            if event.key == K_DOWN:
                mario.move_down = True
                mario.move_up = False
        if event.type == KEYUP:
            if event.key == K_LEFT:
                mario.move_left = False
            if event.key == K_RIGHT:
                mario.move_right == False
            if event.key == K_UP:
                mario.move_up == False 
            if event.key == K_DOWN:
                mario.move_down == False 
        if event.type == MOUSEMOTION:
            mario.centerx = event.pos[0]
            mario.centery = event.pos[1]
     
     ## go through game loop and add koopas 
    koopa_add += 1 
    if koopa_add == koopa_bad_rate:
        koopa_add = 0
        koopas = generateKoopa()
    
    # move mario 
#    if moveLeft and mario.body.left >0:
#        mario.body.left -= mario.move_rate
#    if moveRight and mario.body.right < window_width:
#        mario.body.left += mario.move_rate
#    if moveUp and mario.body.top > 0 :
#        mario.body.top -= mario.move_rate 
#    if moveDown and mario.body.top < window_height:
#        mario.body.top += mario.move_rate 
    mario.move(window_width, window_height)         

    # move peach 
    peach.move(window_surface)
        
    # move koopa 
    for k in koopas:
        moveKoopa(k, peach.body)
       
    # draw game world 
    window_surface.fill(background)
    drawText("Score : %s" % (score), font, window_surface, 450, 510)
    drawText("Top Score : %s" % (topscore), font, window_surface, 450,540)
    
    # draw mario's updated position 
    mario.draw_character(window_surface)
    
    # draw peach's updated position 
    peach.draw_character(window_surface) 
    
    # draw koopas 
    for k in koopas:
        window_surface.blit(k["surface"], k["rect"])
    
    mario_removes_koopa() 
        
    pygame.display.update()
    
    # check if koopa hit peach 
    if did_koopa_reach_peach():
        if score > topscore:
            topscore = score 
        drawText("Game Over!", font, window_surface, window_width/3, window_height/3)
        time.sleep(5)
        terminate()
    
    # setting game speed 
    mainClock.tick(fps)
    

#terminate()
    
    
    
        
    
         
    


    


