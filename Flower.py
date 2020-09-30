
import pygame, random 
from ImageAbstract import Image 

class Flower(Image): 

    min_size = 15 
    max_size = 20

    def __init__(self, window_surface):
        self.size = random.randint(self.min_size, self.max_size) 
        self.image = pygame.image.load("images/flower.png") 
        self.body = self._generate_body(window_surface) 

    def _generate_body(self, window_surface):
        left = random.randint(0, window_surface.get_width()) 
        top = random.randint(window_surface.get_height() * (3/4), window_surface.get_height()) 
        return pygame.Rect(left, top, self.size, self.size) 

    def stretch(self):
        return super().stretch() 

    def draw_character(self, screen):
        super().draw_character(screen) 



