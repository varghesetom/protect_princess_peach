
import pygame, random 

class Nintendo:
    def __init__(self,left, top, width, height, speed_min=0, speed_max=0, minsize=0, maxsize=0):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.minsize = minsize 
        self.maxsize = maxsize 
        self.body = self.rectFrame()
        
    def rectFrame(self):
        return pygame.Rect(self.left, self.top, self.width, self.height)
    
    def hit_koopa(self, koopa):
        if self.body.colliderect(koopa["rect"]):
            return True
        return False 

    def stretch(self):
        return pygame.transform.scale(self.image, (40,40))
    
    def draw_character(self, screen):
        screen.blit(self.stretch(), self.body) 


class Mario(Nintendo):

    def __init__(self,left, top, width, height):
        super().__init__(left, top, width, height)
        self.move_rate = 5
        self.move_left = False 
        self.move_right = False 
        self.move_up = False 
        self.move_down = False 
        self.image = pygame.image.load("images/mario.bmp")

    def move(self, window_width, window_height):
        if self.move_left and self.body.left > 0:
            self.body.left -= self.move_rate 
        if self.move_right and self.body.right < window_width:
            self.body.left += self.move_rate 
        if self.move_up and self.body.top > 0:
            self.body.top -= self.move_rate 
        if self.move_down and self.body.top < window_height:
            self.body.top += self.move_rate 


class Peach(Nintendo):

    def __init__(self,left, top, width, height,speed_min=0, speed_max=0, minsize=0, maxsize=0):
        super().__init__(left, top, width, height)
        self.image = pygame.image.load("images/peach.bmp") 

    def move(self, window_surface):
        self.body.left += random.randint(-10, 10)
        self.body.top += random.randint(-10, 10)
        self.body.clamp_ip(window_surface.get_rect()) 


if __name__  == "__main__":
    Nintendo()
    Mario(Nintendo)
        
