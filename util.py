
import pygame, sys
from settings import * 

def terminate():
    pygame.quit()
    sys.exit()
    
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, text_color)  ## defining the text object with font and color 
    textrect = textobj.get_rect() # getting size and location of this text object 
    textrect.topleft = (x,y) ## setting the location of the text object 
    surface.blit(textobj, textrect) ## displaying the textobject at the text location 


