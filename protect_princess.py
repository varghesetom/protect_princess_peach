#!/usr/bin/env python
'''
Protect Princess Peach from the Koopas as she picks up flowers! 
'''

import pygame, random, sys, math, copy, time
from Characters import Nintendo, Mario

from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()
    
#Use the [:] to create a copy so as not to mess up the other processes of adding koopas 

def peachHitKoopa(peach, koopas):
    for k in koopas:
        if peach.colliderect(k["rect"]):
            return True 
    return False  

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
    
def movePeach(peach):
    left = random.randint(-10,10)
    top = random.randint(-10,10)
    peach.left += left
    peach.top += top
    peach.clamp_ip(window_surface.get_rect())
    

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
# set up font 
font = pygame.font.SysFont(None,30) # default font aet at 30 points 
# show start screen
window_surface.fill(background)
drawText("Protect Princess Peach!" , font, window_surface, window_width/2, window_height/2)
pygame.display.update()

# set up images and characters 
# mario 
m = Mario(left=100, top =100, 
          width = 40, height =40)
#mario = m.rectFrame()
marioStretched = m.stretch()

#mario = pygame.Rect(100, 100, 40, 40)
#mario_move_rate = 5
#marioImage = pygame.image.load("images/mario.bmp")
#marioStretched = pygame.transform.scale(marioImage, (40,40))

## peach characteristics
peach = pygame.Rect(200, 500, 40, 40)
peachImage = pygame.image.load("images/peach.bmp")
peachStretched = pygame.transform.scale(peachImage, (40,40)) 

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
moveLeft = moveRight = moveUp = moveDown = False 
score = 0 


# set up game loop 
while True:
    score += 1
    ## go through event loop 
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYDOWN:
            if event.type == moveLeft:
                moveLeft = True 
            if event.type == moveRight:
                moveRight = True
            if event.type == moveUp:
                moveUp = True 
            if event.type == moveDown:
                moveDown = True
        if event.type == KEYUP:
            if event.type == moveLeft:
                moveLeft = False
            if event.type == moveRight:
                moveRight == False
            if event.type == moveUp:
                moveUp == False 
            if event.type == moveDown:
                moveDown == False 
        if event.type == MOUSEMOTION:
            mario.centerx = event.pos[0]
            mario.centery = event.pos[1]
     
     ## go through game loop and add koopas 
    koopa_add += 1 
    if koopa_add == koopa_bad_rate:
        koopa_add = 0
        koopas = generateKoopa()
    
    # move mario 
    if moveLeft and mario.body.left >0:
        mario.body.left -= m.move_rate
    if moveRight and mario.body.right < window_width:
        mario.body.left += m.move_rate
    if moveUp and mario.body.top > 0 :
        mario.body.top -= m.move_rate 
    if moveDown and mario.body.top < window_height:
        mario.body.top += m.move_rate 
        
    # move peach 
    movePeach(peach)
        
    # move koopa 
    for k in koopas:
        moveKoopa(k, peach)
        
    # delete koopas if mario hits them. 
    for k in koopas[:]:
        if m.hitKoopa(mario, k):
            koopas.remove(k)
    
    # draw game world 
    window_surface.fill(background)
    drawText("Score : %s" % (score), font, window_surface, 450, 510)
    drawText("Top Score : %s" % (topscore), font, window_surface, 450,540)
    
    # draw mario 
    m.drawCharacter(window_surface, marioStretched, mario)
    
    # draw peach
    window_surface.blit(peachStretched, peach)
    
    # draw koopas 
    for k in koopas:
        window_surface.blit(k["surface"], k["rect"])
        
    pygame.display.update()
    
    # check if koopa hit peach 
    if peachHitKoopa(peach, koopas):
        if score > topscore:
            topscore = score 
        drawText("Game Over!", font, window_surface, window_width/3, window_height/3)
        time.sleep(5)
        terminate()
#        break
    
    # setting game speed 
    mainClock.tick(fps)
    

#terminate()
    
    
    
        
    
         
    


    


